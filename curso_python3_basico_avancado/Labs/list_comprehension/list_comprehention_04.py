# Entendendo list comprehension

numeros = [1, 2, 3, 4, 5]
# novos_numeros = numeros.copy()

# numeros[0] = 20
# print(novos_numeros)

# Fazendo com List comprehension

novos_numeros = [numero for numero in numeros] # agora minha lista não é alterada

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)
    
numeros[0] = 150

print(novos_numeros)
print(numeros)
