# Empacotamento e desempacotamento de dicionários

a, b = 1, 2 # empacotamento
a, b = b, a # invertendo os valores
# print(a, b)

cadastro = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho',
}

a, b = cadastro
print(a, b)