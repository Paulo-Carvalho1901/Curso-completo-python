# Tirando todas as duvidas de list comprehension

# numeros = [1, 2, 3, 4, 5]
# novos_numeros = numeros

# está apenas apontando para mesmo valor na memória
# a lista não está sendo copía para novos_ numeros, apenas referencia 
# o mesmo valor.

# novos_numeros[0] = 999
# print(numeros)

#############################################################################
# Fazendo uma shallow copy (copia rasa dos itens)

numeros = [1, 2, 3, 4, 5]
novos_numeros = numeros.copy()


numeros[0] = 20
print(numeros)
print(novos_numeros)
