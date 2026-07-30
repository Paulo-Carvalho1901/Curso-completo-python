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

# mostrando_na_tela(novos_produtos)

###########################################################################

# Gerando uma lista
# como faria essa lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(10)))

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(lista)

# def cria_lista():
#     lista = []
#     for numero in range(10):
#         # criar uma lógica para acumular os numeros
#         lista.append(numero)
#     return lista

# l1 = cria_lista()
# print(l1)

##############################################################################
# Lista comprehension
lista = [n for n in range(10) if n < 5]
print(lista)
