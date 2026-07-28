# Empacotamento e desempacotamento de dicionários

a, b = 1, 2 # empacotamento
a, b = b, a # invertendo os valores
# print(a, b)

cadastro = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho',
}

# a metodos items() retorna chave e valor do dict
(a1, a2), (b1, b2) = cadastro.items()
print(a1, a2)
print(b1, b2)
