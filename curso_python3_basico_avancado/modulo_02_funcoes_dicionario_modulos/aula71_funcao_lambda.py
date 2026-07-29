# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [32, 2, 5, 55, 4, 8, 10, 0, 1, 2, 3]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Função chave que irar ordenanr dicionario.
# def ordena(item):
#     return item['nome']

# Nesta estou utilizando a função ordena
# para gerar a ordenação do dicionario.
# lista.sort(key=ordena) # fazendo a ordenação
# print(lista)

# Organizando para melhor os dados com for.
# for item in lista:
#     print(item)

###############################################################################

# Expressão lambda
# no caso o primeiro item é parâmetro e segundo item é retorno da função
# lista.sort(key=lambda item: item['nome'])

# Organizando para melhor os dados com for
# for item in lista:
#     print(item)


###############################################################################
# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)
