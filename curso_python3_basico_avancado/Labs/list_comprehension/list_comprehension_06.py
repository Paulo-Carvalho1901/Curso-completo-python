# List comprehension com filter

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros if numero > 5]


numeros[0] = 54

print(numeros)
print(novos_numeros)
