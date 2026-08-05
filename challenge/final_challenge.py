from openai import OpenAI
import json
from challenge.contato_com_llm import recebe_linha_retorna_json

lista_de_listas = []

with open('resenhas_app.txt', 'r', encoding='utf-8') as f:
    for i in f:
        lista_de_listas.append(i)

lista_de_resenhas_json = []

for resenha in lista_de_listas:
    resenha_json = recebe_linha_retorna_json(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

def contador_e_juntador(lista_de_dicts):
    contador_positivas = 0
    contador_neutras = 0
    contador_negativas = 0

    for dict in lista_de_dicts:
        if dict['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dict['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1

    textos_unidos = "#####".join(lista_de_dicts)
    return contador_positivas, contador_neutras, contador_negativas, textos_unidos

avaliacoes_positivas, avaliacoes_neutras, avaliacoes_negativas, textos = contador_e_juntador(lista_de_resenhas_json)