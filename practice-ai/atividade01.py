from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

chave_api = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

mensagem = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[

        {
            "role": "user", "content": "Me fale quais ingredientes são necessários para fazer um bolo."
        }

    ]
)

print(mensagem.content[0].text)