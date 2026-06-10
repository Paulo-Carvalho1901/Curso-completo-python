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
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['Sobrenome'])

# print('ISSO TESTE!')