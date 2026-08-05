# Generator expression, Iterables and Iterator in Python
# Basicamente são funções que sabem quando pausar.

iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable) # Have __iter__ and __next__

# List comprehension
# generator = [numero for numero in range(10)]

# Generator expression - next(generator)
generator = (numero for numero in range(10))

print(next(generator))
