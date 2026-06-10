# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

# Adicionando um item no dicionário
chave = 'nome'

pessoa[chave] = 'Paulo Roberto'
pessoa['Sobrenome'] = 'Carvalho'

# Alterando o valor da chave
pessoa[chave] = 'Andreia'

# Apagando uma chave
del pessoa['Sobrenome']

print(pessoa)
