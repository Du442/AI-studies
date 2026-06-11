ativo = True

from dotenv import load_dotenv
import os
import anthropic

def digite_clear():
    input("\nDigite uma tecla para prosseguir: ")
    os.system('cls')

load_dotenv()

chave_api = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

while ativo:
    pergunta = str(input("Escreva a pergunta que deseja realizar ao modelo: ")).lower()
    if pergunta == "sair":
        print("\nApp finalizado")
        os.system('cls')
        break
    resposta = client.messages.create(
        max_tokens=1024,
        model="claude-haiku-4-5-20251001",
        messages=[

            {
                "role": "user", "content": pergunta
            }

        ]
    )
    print(resposta.content[0].text)
    digite_clear()
    

