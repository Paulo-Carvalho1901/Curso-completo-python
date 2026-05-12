# Listas de listas e seus indices

salas = [
    # 0        1 
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduardo', (0, 10, 20, 30, 40)], # 2 
]

# print(salas[2][3][2])

for sala in salas:
    print(sala)