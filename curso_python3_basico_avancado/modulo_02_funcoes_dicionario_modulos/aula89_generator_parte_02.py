# Introdução às Generator functions em python
# generator = (n for n in range(1000))

# OBS: todo generator é um iterator

def generator(n=0):
    yield 1 # Pausar
    return 'Acabou'


gen1 = generator(n=0)
print(gen1)
