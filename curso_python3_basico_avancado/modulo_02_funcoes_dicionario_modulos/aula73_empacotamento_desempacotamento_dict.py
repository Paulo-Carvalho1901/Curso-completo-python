# Empacotamento de desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho'
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
