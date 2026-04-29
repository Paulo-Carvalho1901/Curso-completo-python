"""
Introdução ao desempacotamento + tuples (tuplas)
"""

"""
nomes = ['Maria', 'Helena','Luiz']

formas de desempacotar
nome1, nome2, nome3 = nomes

nome1, nome2, nome3 = ['Maria', 'Helena','Luiz']

pegando apenas um valor de cada vez do pacote

_, _, nome3 = ['Maria', 'Helena','Luiz']
_, nome2, _ = ['Maria', 'Helena','Luiz']
nome1, _, _ = ['Maria', 'Helena','Luiz']

variavel resto cria um novo pacote dos valores que não
estiver sendo utilizado
nome1, *resto = ['Maria', 'Helena','Luiz']

"""

_, _, nome3 = ['Maria', 'Helena','Luiz']
print(nome3)
