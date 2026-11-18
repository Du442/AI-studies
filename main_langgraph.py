from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal, TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
import asyncio
import os

load_dotenv()

class Route(TypedDict):
    destiny: Literal["beach", "mountain"]

class State(TypedDict):
    query: str
    destiny: Route
    answer: str

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt_consultor_beach = ChatPromptTemplate.from_messages(
    [
        ("system", "Introduce yourself as a Ms Praia. You are a travel specialist in beaches areas"),
        ("human", "{query}")
    ]
)

prompt_consultor_mountain = ChatPromptTemplate.from_messages(
    [
        ("system", "Introduce yourself as a Ms Montanha. You are a travel specialist in mountain areas and radical activities"),
        ("human", "{query}")
    ]
)

chain_beach = prompt_consultor_beach | model | StrOutputParser()
chain_mountain = prompt_consultor_mountain | model | StrOutputParser()

prompt_router = ChatPromptTemplate.from_messages(
    [
        ("system", "Answer only with 'beach' or 'mountain'."),
        ("human", "{query}")
    ]
)

router = prompt_router | model.with_structured_output(Route)

async def no_router(state: State, config=RunnableConfig):
    return {"destiny": await router.ainvoke({"query": state["query"]}, config)}

async def no_beach(state: State, config=RunnableConfig):
    return {"destiny": await chain_beach.ainvoke({"query": state["query"]}, config)}

async def no_mountain(state: State, config=RunnableConfig):
    return {"destiny": await chain_mountain.ainvoke({"query": state["query"]}, config)}

def no_chooser(state:State) -> Literal["beach", "mountain"]:
    return "beach" if state["destiny"]["destiny"] == "beach" else "mountain"

graph = StateGraph(State)
graph.add_node("route", no_router)
graph.add_node("beach", no_beach)
graph.add_node("mountain", no_mountain)

graph.add_edge(START, "route")
graph.add_conditional_edges("route", no_chooser)
graph.add_edge("beach", END)
graph.add_edge("mountain", END)

app = graph.compile()

async def main():
    response = await app.ainvoke(
        {
            "query": "I wanna visit somewhere in brazil, with a good culture and beaches."
        }
    )
    print(response["answer"])

asyncio.run(main())