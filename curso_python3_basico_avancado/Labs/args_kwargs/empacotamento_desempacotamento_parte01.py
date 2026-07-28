# Empacotamento e desempacotamento de dicionários

a, b = 1, 2 # empacotamento
a, b = b, a # invertendo os valores
# print(a, b)

# cadastro = {
#     'nome': 'Paulo',
#     'sobrenome': 'Carvalho',
# }

# UMA FORMA DE SE DESEMPACOTAR
# a metodos items() retorna chave e valor do dict
# (a1, a2), (b1, b2) = cadastro.items()
# print(a1, a2)
# print(b1, b2)

#########################################################################

# OUTRA FORMA DE SE DESEMPACOTAR
# for chave, valor in cadastro.items():
#     print(chave, valor)

##########################################################################

# MAIS UMA MANEIRA DE SE PENSAR EM EMPACOTAMENTO E DESEMPACOTAMENTO

cadastro = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho',
}
