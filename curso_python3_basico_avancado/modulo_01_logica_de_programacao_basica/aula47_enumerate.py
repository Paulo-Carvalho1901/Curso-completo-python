"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# # lista_enumerada = list(enumerate(lista))

for indice, nome in enumerate(lista):
    print(indice, nome)

# for itens in enumerate(lista):
#     indice, nome = itens
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
