# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

# Exemplo com shallow copy dicionario
print('Dict')
d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2]
}

# Criando copia rasa
# copia rasa vale apenas para valores imutavel (str, int, float, bool, tuple)
# agora quando os dados são mutavel, no caso como lista e dict
# o o que acontece é que ele apenas aponta para esse mesmo valor na memoria da lista

# d2 = copy.copy(d1) # ou d1.copy() ambos são copia rasa 
d2 = copy.deepcopy(d1) # copia profunda

d2['c1'] = 1000
d2['li'][0] = 9999

print('d1', d1)
print('d2', d2)

print()
print('Lista')
# Exemplo com lista shallow copy (copia rasa)
lista1 = [1, 2, 3, 4]
lista2 = lista1

lista2[0] = 10 # tambem afeta a lista1, pois são o mesmo valor na memoria

print('lista1', lista1, 'id', id(lista1))
print('lista2', lista2, 'id', id(lista2))
