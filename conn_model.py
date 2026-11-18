from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def ai() -> ChatOpenAI | None:
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    if not model:
        return None
    return model