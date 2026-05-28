def minusculo(texto):
    return texto.lower()


def maiusculo(texto):
    return texto.upper()


def aplica(function, texto):
    return function(texto)


print(aplica(maiusculo, 'paulo'))
print(aplica(minusculo, 'PAULO'))
