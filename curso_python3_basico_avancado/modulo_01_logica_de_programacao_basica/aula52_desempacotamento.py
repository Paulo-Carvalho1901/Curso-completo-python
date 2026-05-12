# Desempacotamento em chamadas
# de métodos e função
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'legal'

salas = [
    # 0        1 
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduardo', ], # 2 
]

# Desempacotamento
# a, b, *_, c = lista
# print(a, c)

# Desenpacotando a lista com for
for itens in lista:
    print(itens, end=' ')
print()

# Obtendo o mesmo resultado que for
# desempacotandoa lista
print('Maria', 'Helena', 1, 2, 3, 'Eduarda') # A mesma ideia do desempacotamento
print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')