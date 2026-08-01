# Dictionary comprehension e set comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
}

# print(dc)

############################################################################

lista = [
    ('a', 'valor'),
    ('b', 'valor'),
    ('c', 'valor'),
]

dc2 = {
    chave: valor
    for chave, valor in lista
}

# print(dc2)

############################################################################
# Set Comprehension

set1 = {i for i in range(10)}
print(set1)
