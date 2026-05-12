# Desempacotamento em chamadas
# de métodos e função
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'legal'

# Desempacotamento
# a, b, *_, c = lista
# print(a, c)

# Desenpacotando a lista com for
for itens in lista:
    print(itens, end=' ')
print()

# Obtendo o mesmo resultado que for
# desempacotandoa lista
print(*lista)