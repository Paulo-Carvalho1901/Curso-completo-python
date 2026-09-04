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

numeros = [random.randint(1, 10) for _ in range(20)]
print(numeros)

# Exemplo 2
# Agora imagine que ja tenha uma lista de inteiros
# vamos pegar a lista que criamos no exemplo anterior
# e queira obter uma nova lista a partir dela
# que contenha apenas numeros pares

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)

# Exemplo 3
# Você tem uma string e deseja remover todos os caracteres
# que não forem letra ou espaço
# EX: py(tho@n ol!a !mun@do => python ola mundo

string = 'py(tho@n ol!a !mun@do'

string_formatada = ''
for letra in string:
    if letra.isalpha() or letra == ' ':
        string_formatada += letra

print(string_formatada)

nova_string = ''.join([letra for letra in string if letra.isspace() or letra.isalpha()])
print(nova_string)
