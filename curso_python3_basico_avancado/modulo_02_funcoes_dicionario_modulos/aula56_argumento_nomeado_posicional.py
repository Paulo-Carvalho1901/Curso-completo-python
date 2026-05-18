"""
Argumento nomeado e não nomeado em função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Argumentos posicionais
def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y =', x + y)

soma(1, 3)
soma(2, 1)
