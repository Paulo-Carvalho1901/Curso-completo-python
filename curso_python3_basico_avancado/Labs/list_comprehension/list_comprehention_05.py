# Entendendo list comprehension
numeros = [1, 2, 3, 4, 5]

novos_numeros = [numero for numero in numeros]

numeros[1] = 88
print(numeros)
print(novos_numeros)
