from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import Field, BaseModel
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
from langchain_core.globals import set_debug
import os

set_debug(True)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

class JsonOutput(BaseModel):
    city: str = Field("City recommended to visit")
    reason: str = Field("Why the reason to visit this city")

class Restaurants(BaseModel):
    city: str = Field("City recommended to visit")
    restaurants: str = Field("Restaurant recommended to visit in the city")

parseator = JsonOutputParser(pydantic_model=JsonOutput)
restaurant_parseator = JsonOutputParser(pydantic_model=Restaurants)

city_prompt = PromptTemplate(
    template="""
    Give me a city by my interest {interest},
    {exit_format}
    """,
    input_variables=["interest"],
    partial_variables={"exit_format": parseator.get_format_instructions()}
)

restaurant_prompt = PromptTemplate(
    template="""
    Gimme some hints of popular restaurants in {city},
    {exit_format}
    """,
    input_variables=["interest"],
    partial_variables={"exit_format": restaurant_parseator.get_format_instructions()}
)

culture_prompt = PromptTemplate(
    template="Gimme some hints of cultural locals in {city}"
)

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

# -- Chains -- #

chain_1 = city_prompt | model | parseator
chain_2 = restaurant_prompt | model | restaurant_parseator
chain_3 = culture_prompt | model | StrOutputParser()

chain = (chain_1 | chain_2 | chain_3)

response = chain.invoke(
    {
        "interest": "beaches"
    }
)
print(response)