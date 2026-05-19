"""
Argumento nomeado e não nomeado em função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Argumentos posicionais
def soma(x, y): # parametros (x, y)
    print(f'{x=} y={y}', '|', 'x + y =', x + y)


soma(1, 3) # argumento posicional (é passado de acordo com posição)
soma(y=2, x=1) # argumentos nomeados (é passo pelo nome dos paramatros no argumento)
