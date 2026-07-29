# List comprehension

# criado uma lista
print(list(range(10)))

# uma forma de criar uma lista
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# list comprehension
lista = [numero for numero in range(10)]
print(lista)
