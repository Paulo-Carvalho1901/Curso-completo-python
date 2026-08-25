"""
Funções nomeadas em Python
"""

def div(x, y):
    """Função que soma dois valores"""
    return x / y


# print(list(map(lambda x: x + 2, [1, 2, 3])))

# Função anônima
soma = lambda x: x + 2
print(soma(2))

# Funções de classe

class classe_soma:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __call__(self):
        return self.x + self.y



