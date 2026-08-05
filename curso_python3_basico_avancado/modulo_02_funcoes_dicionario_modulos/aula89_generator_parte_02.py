# Introdução às Generator functions em python
# generator = (n for n in range(1000))

# OBS: todo generator é um iterator

def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2
    print('Mais uma chamada...')
    yield 3
    

gen = generator(n=0)
# print(gen1.__iter__())
print(next(gen))
print(next(gen))
