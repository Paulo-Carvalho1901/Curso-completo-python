# List comprehension

numeros = [1, 2, 3, 4, 5]

# criado list comprehension
# novos_numeros = [numero for numero in numeros]
divisao = [numero / 2 for numero in numeros]

# alterando a lista numeros
numeros[0] = 20

print('numeros', numeros)
print('novos_numeros', divisao)
