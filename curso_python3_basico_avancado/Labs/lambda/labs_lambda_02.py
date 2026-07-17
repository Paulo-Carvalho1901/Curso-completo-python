# https://hub.asimov.academy/blog/lambda-python/
# Funções lambda são uma ferramenta elegante do Python que 
# permite criar funções anônimas (sem nome) de forma concisa. São ideais para 
# operações simples e únicas onde uma função completa seria excessiva.

# Como criar Funções lambda

# Uma função lambda é criada usando a palavra-chave lambda,
# seguida de um ou mais argumentos, e uma expressão:

# (argumentos) são os dados de entrada que esta função irá receber
# (expressão) é o código que será executado quando a função lambda for chamada.

# Sua sintaxe básica é a seguinte:
# lambda {argumentos}: {expressão}

# exemplo 1:
soma = lambda x, y: x + y
print(soma(2, 3))

# Os argumentos são 2: x e y
# A expressão a ser executada: x + y

# exemplo 2:
minha_lista = [('maça', 2), ('banana', 1), ('laranja', 3)]
minha_lista_ordenada = sorted(minha_lista, key=lambda x: x[1])
print(minha_lista_ordenada)


# # exemplo 3:
def multiplica(x, y):
    """multiplica dois numeros"""
    resultado = x * y
    return resultado


print(multiplica(2, 3))

# Lambda
multiplicar = lambda x, y: x * y
print(multiplicar(2, 10))


# exemplo 4:
notas = {'Ana': 9, 'Bato': 7, 'Carlos': 8}

notas_ordenadas = sorted(
    notas.items(),
    key=lambda tupla: tupla[1]
)
print(notas_ordenadas)
