# List comprehension

# Comparação rápida
# Forma tradicional

lista = []
for x in range(5):
    lista.append(x * 2)
print(lista)

# Com list comprehension
lista = [x * 2 for x in range(5)]
print(lista)

# criado uma lista
# print(list(range(10)))

# uma forma de criar uma lista
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# list comprehension
lista = [numero for numero in range(10)]
# print(lista)
