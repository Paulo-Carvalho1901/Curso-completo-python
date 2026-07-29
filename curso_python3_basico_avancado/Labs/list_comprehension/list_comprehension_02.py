# List Comprehension é uma forma mais curta e elegante de criar listas em Python.

# Sem list comprehension:
numeros = [1, 2, 3, 4, 5]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# print(quadrado)

##############################################################################

# com list comprehension:
numeros = [1, 2, 3, 4, 5]
quadrado = [numero ** 2 for numero in numeros]
# print(quadrado)

###############################################################################

# Sintaxe
# [expressao for item in iteravel]

nomes = ['Ana', 'João', 'Maria']
letra_maiuscula = [nome.upper() for nome in nomes]
# print(letra_maiuscula)

##############################################################################

# Usando condições (if)
# Você pode filtrar elementos:

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)

##############################################################################

# Usando if/else
# Também é possível transformar os valores de acordo com uma condição:

numeros = [1, 2, 3, 4, 5]

resultado = ["par" if numero % 2 == 0 else "impar" for numero in numeros]
print(resultado)
