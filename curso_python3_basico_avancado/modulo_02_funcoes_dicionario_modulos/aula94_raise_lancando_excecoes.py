# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        return n


print(divide(8, 0))
