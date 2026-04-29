# Tipo tupla - uma lista imutável

"""
Geralmente utilizamos as tuplas:

    Caso que você não precise alterar nemhum dados na 
    lista se utiliza tuplas pois é um estrutura de dados
    imutável 
"""

# Criando uma tupla 
# forma 1
nomes = 'João', 'Helena', 'Maria'
print(nomes[0])
print(nomes[-1])
print(nomes)

# forma 2
nomes = ('João', 'Helena', 'Maria')
print(nomes)

# Forma 3 - fazendo a coerção de uma lista para tupla
nomes = ['João', 'Helena', 'Maria']
print(type(nomes))
nomes = tuple(nomes)
print(nomes)
print(type(nomes))
