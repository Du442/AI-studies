from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

chave_api = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

nome_user = str(input("Digite seu nome aqui: "))
pergunta_user = str(input("Digite a pergunta que você deseja realizar ao modelo: "))

resposta = client.messages.create(
    max_tokens=1024,
    model="claude-haiku-4-5-20251001",
    messages=[
        {
            "role": "system", "content": f"Sempre mencione com meu nome {nome_user} ao inicio da resposta",
            "role": "user", "content": pergunta_user
        }
    ]
)

print(resposta.content[0].text)