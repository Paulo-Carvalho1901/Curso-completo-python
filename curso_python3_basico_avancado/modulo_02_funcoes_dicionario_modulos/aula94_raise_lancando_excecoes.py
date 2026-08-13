# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce está tendando dividir por zero.')


def divide(n, d):
    nao_aceito_zero(d)
    return n / d

print(divide(8, 0))
