from final_challenge import lista_de_listas
from openai import OpenAI

client = OpenAI(
    api_key='lm-studio',
    base_url='http-address'
)

def recebe_linha_retorna_json(linha):

    resposta = client.responses.create(
        model='gpt-5.6',
        reasoning={'effort': 'low'},
        instructions='Você ao final do prompt terá que obrigatóriamente me retornar em formato JSON.',
        input=f'''Eu irei te enviar uma lista com diferentes linhas e que em cada uma possui um USUARIO, a RESENHA, e na mesma resenha uma avaliação.

        Quero que você pegue essa lista linha por linha e desejo que transforme em um json onde teve que cada item do JSON terá obrigatóriamente que ter:

        'usuario': 'Nome do usuario que enviou a resenha',
        'resenha_original': 'A resenha do jeito que foi enviada sem nenhuma tradução, ela natural.',
        'resenha_pt': 'Resenha traduzida para portugues do Brasil.',
        'avaliacao': 'A avaliação dada pelo usuario durante a resenha.'

        aqui o elemento: {linha}

        após realizar a transformação de todas as linhas e juntadas em um JSON apenas retorne-o.

        '''
    )
    return resposta.output_text