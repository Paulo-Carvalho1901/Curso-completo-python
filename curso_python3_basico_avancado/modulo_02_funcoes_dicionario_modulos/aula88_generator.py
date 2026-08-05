# Generator expression, Iterables and Iterator in Python
# Basicamente são funções que sabem quando pausar.

import sys

iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable) # Have __iter__ and __next__

# List comprehension
lista = [numero for numero in range(10)]

# Varificando varios valores na memória
for n in [10, 100, 1000, 10000]:
    lista = [i for i in range(n)]
    print(n, sys.getsizeof(lista))
print()

# Generator expression - next(generator)
generator = (numero for numero in range(10))

print(sys.getsizeof(lista)) # vendo tamaho da lista em byte
print(sys.getsizeof(generator))
