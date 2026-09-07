# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

# criando dict
pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho',
    'idade': 37,
    'altura': 1.80,
    'endereço': [
        {'Rua': 'tal tal', 'numero': 353},
        {'Rua': 'outra rua', 'numero': 151},
    ]
}

# criando dict não muito usada hoje
# pessoa = dict(nome='Marcio', sobrenome='Silva')

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
