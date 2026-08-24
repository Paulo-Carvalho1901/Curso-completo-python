"""
Funções nomeadas em Python
"""

def div(x, y):
    """Função que soma dois valores"""
    return x / y


# print(soma.__name__)
# print(dir(soma))
# print(soma.__doc__)
# print(help(soma))

try:
    print(div(0, 0))
except:
    print(div.__name__)
