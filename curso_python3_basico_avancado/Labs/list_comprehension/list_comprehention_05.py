# Entendendo list comprehension
numeros = [1, 2, 3, 4, 5]

divisao = [numero / 2 for numero in numeros]

numeros[1] = 88
print(numeros)
print(divisao)
