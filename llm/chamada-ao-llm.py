from email import message
from openai import OpenAI

client = OpenAI(
    base_url='localhost',
    api_key='llm'
)

response = client.chat.completions.create(
    model='google/gemma-3-1b',
    messages=[
        {
            'role':'system',
            'content':'Você é um assitente de IA prestivado e bem humorado.'
        },
        {
            'role':'user',
            'content':'O que é a IA Generativa?'
        }
    ],
    temperature=1.0
)

print(response.choices[0].message.content)