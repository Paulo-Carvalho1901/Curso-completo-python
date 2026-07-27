# Empacotamento de desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Paulo',
#     'sobrenome': 'Carvalho'
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho'
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoas}

print(pessoa_completa)
