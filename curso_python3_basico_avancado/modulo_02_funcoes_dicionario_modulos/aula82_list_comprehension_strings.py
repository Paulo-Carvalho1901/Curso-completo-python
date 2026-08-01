# list comprehension
# trabalhando com strings

string = 'Paulo Carvalho'

numeros_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numeros_de_letras]
    for indice in range(0, len(string), numeros_de_letras)
])

# print(nova_string)

##########################################################################

nomes = ['paulo', 'andreia', 'davi', 'joão', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]

print(novos_nomes)
