import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

lista_pergunta = [
    "Quero visitar um lugar no brasil, famoso por praias e culturas. Pode sugerir?",
    "Qual a melhor epoca do ano para ir?"
]

for i in lista_pergunta:
    resposta = modelo.invoke(i)
    print("Usuario: ", i),
    print("IA: ", resposta.content, "\n")