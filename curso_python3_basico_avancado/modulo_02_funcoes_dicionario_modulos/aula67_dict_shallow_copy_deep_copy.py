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

# Exemplo com shallow copy dicionario
print('Dict')
d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1
d2['c1'] = 1000
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
