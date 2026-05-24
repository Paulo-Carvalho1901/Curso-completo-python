# Args - Argumentos não nomeados

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 125, 25, 25
soma_geral = soma(*numeros)
print(soma_geral)

# Função interna do Python (sum)
print(sum(numeros))
