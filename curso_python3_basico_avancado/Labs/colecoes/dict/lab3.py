# Manipulando chave e valores em dicionarios

pessoa = {}

chave = 'nome'


# add um chave e valor no dict
pessoa[chave] = 'Paulo Carvalho'
pessoa['sobrenome'] = 'Carvalho'


print(pessoa[chave])

# Alterando valor da dict pela chave
pessoa[chave] = 'Andreia Cristina'

# Apagando uma chave
del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])
