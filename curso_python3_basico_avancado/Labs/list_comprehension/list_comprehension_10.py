# Imagine que voce precise criar
# uma lista com 20 números aleatórios inteiros,
# entre 0 e 20 como faria isso?

import random

# 1° forma
# lista_20_numeros_inteiros = random.randint(0, 20)
# print(lista_20_numeros_inteiros)

# 1° forma de resolver
numeros = []
for i in range(20):
    numeros_randomicos = random.randint(1, 10)
    numeros.append(numeros_randomicos)

print(numeros)

# 2° forma de resolver
# List comprehension
# Estrutura da lista comprehension
# [o que você quer na lista] for i in range(n)

print([random.randint(1, 10) for _ in range(20)])
