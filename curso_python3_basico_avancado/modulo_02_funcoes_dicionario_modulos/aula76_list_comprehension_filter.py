# Filtro de dados em list comprehension

import pprint


def mostrando_na_tela(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    # Mapeamento list comprehension
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')

mostrando_na_tela(novos_produtos)
