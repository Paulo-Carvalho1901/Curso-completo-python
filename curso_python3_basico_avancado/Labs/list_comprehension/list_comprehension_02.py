# List Comprehension é uma forma mais curta e elegante de criar listas em Python.

# Sem list comprehension:
numeros = [1, 2, 3, 4, 5]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)
