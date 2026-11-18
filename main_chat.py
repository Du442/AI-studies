from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

suggestion_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a travel guide specialized in brazilian destiny. Introduce yourself as a Mr. Passeios"),
        ("placeholder", "{historic}"),
        ("human", "{query}")
    ]
)

chain = suggestion_prompt | model | StrOutputParser()

memory = {}
session = "langchain_class"

def historic_by_session(session: str):
    if session not in memory:
        memory[session] = InMemoryChatMessageHistory()
    return memory[session]

questions = [
    "I wanna visit a place in brazil, famous by beaches and cultures. Can you suggest one?",
    "Which the best moment of the year to go?"
]

chain_with_memory = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=historic_by_session,
    input_messages_key="query",
    history_messages_key="historic"
)

for i in questions:
    response = chain_with_memory.invoke(
        {
            "query": i
        },
        config={"session":session}
    )
    print("User: ", i),
    print("IA: ", response, "\n")