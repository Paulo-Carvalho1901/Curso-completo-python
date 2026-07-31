# List comprehension

def divisaoFn(x, y):
    return x / y


def multiplicacaoFn(x, y):
    return x * y


def potenciacaoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]

# criado list comprehension
# novos_numeros = [numero for numero in numeros]
divisao = [divisaoFn(numero, 2) for numero in numeros]
multiplicacao = [multiplicacaoFn(numero, 2) for numero in numeros]
quadrado = [potenciacaoFn(numero, 2) for numero in numeros]

# alterando a lista numeros
numeros[0] = 20

print('lista original', numeros)
print('divisao', divisao)
print('multiplicação', multiplicacao)
print('quadrado', quadrado)
