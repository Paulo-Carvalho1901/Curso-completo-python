# Tirando todas as duvidas de list comprehension

numeros = [1, 2, 3, 4, 5]
novos_numeros = numeros

# está apenas apontando para mesmo valor na memória
# a lista não está sendo copía para novos_ numeros, apenas referencia 
# o mesmo valor.
print(numeros, id(numeros))
print(novos_numeros, id(novos_numeros))
