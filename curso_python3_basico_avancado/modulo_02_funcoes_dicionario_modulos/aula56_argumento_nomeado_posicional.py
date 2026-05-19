"""
Argumento nomeado e não nomeado em função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Argumentos posicionais
def soma(x, y, z): # parametros (x, y)
    print(f'{x=} y={y} z={z}', '|', 'x + y + z =', x + y + z)


soma(1, 3, 3) # argumento posicional (é passado de acordo com posição)
soma(y=2, z=3, x=1) # argumentos nomeados (é passo pelo nome dos paramatros no argumento)

# Observação sempre que você nomear um argumentos todos
# os proximos tem que ser nomeados
soma(1, 2, z=5)