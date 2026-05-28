def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def executa(function, x, y):
    return function(x, y)


print(executa(soma, 2, 3))
print(executa(multiplica, 2, 3))
