# Empacotamento de desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho'
}

a, b = pessoa.values()
print(a, b)
