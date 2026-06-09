from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict, Literal
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
import asyncio
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

prompt_consultor = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sra Praia. Você é uma especialista em viagens com destinos para praia"),
        ("human", "{query}")
    ]
)

prompt_consultor_montanha = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sra Montanha. Você é uma especialista em viagens para montanhas com destinos para montanhas e atividades radicais"),
        ("human", "{query}")
    ]
)

cadeia_praia = prompt_consultor | model | StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | model | StrOutputParser()

class Rote(TypedDict):
    destino: Literal["praia", "montanha"]

prompt_roteador = ChatPromptTemplate(
    [
        ("system", "Responda apenas com 'praia' ou 'montanha'"),
        ("human", "{query}")
    ]
)

roteador = prompt_roteador | model.with_structured_output(Rote)

class Estado(TypedDict):
    query: str
    destino: Rote
    resposta: str

async def no_roteador(estado: Estado, config=RunnableConfig):
    return {"destino":await roteador.ainvoke({"query":estado["query"]}, config)}

async def no_praia(estado: Estado, config=RunnableConfig):
    return {"destino":await cadeia_praia.ainvoke({"query":estado["query"]}, config)}

async def no_montanha(estado: Estado, config=RunnableConfig):
    return {"destino":await cadeia_montanha.ainvoke({"query":estado["query"]}, config)}

def escolher_no(estado:Estado)->Literal["praia", "montanha"]:
    return "praia" if estado['destino']['destino'] == "praia" else "montanha"

grafo = StateGraph(Estado)
grafo.add_node("rotear", no_roteador)
grafo.add_node("praia", no_praia)
grafo.add_node("montanha", no_montanha)

grafo.add_edge(START, "rotear")
grafo.add_conditional_edges("rotear", escolher_no)
grafo.add_edge("praia", END)
grafo.add_edge("montanha", END)

app = grafo.compile()

async def main():
    resposta = await app.ainvoke(
        {"query": "Quero visitar um lugar no brasil famoso por praias e cultura"}
    )
    print(resposta["resposta"])

asyncio.run()