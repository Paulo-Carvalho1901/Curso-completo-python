# Entendendo list comprehension
def divisaoFn(x, y):
    return x / y


def multiplicacaoFn(x, y):
    return x * y


def potenciacaoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]

divisao = [divisaoFn(numero, 2) for numero in numeros]
multiplicacao = [multiplicacaoFn(numero, 2) for numero in numeros]
potenciacao = [potenciacaoFn(numero, 2) for numero in numeros]
soma = [numero + 2 for numero in numeros]

numeros[1] = 88
print(numeros)
print(divisao)
print(multiplicacao)
print(potenciacao)
print(soma)