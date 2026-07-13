# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# set_lista = {100, 10, 10, 1, 2, 2, 3, 65}
# lista_set = list(set_lista)
# lista_set.sort()
# print('transformando em lista', lista_set)

lista = [12, 2, 2, 4, 5, 1, 0]

lista.sort() # ordenando
lista.sort(reverse=True) # mudando a ordem
print(lista)