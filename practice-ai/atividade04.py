from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

chave_api = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

