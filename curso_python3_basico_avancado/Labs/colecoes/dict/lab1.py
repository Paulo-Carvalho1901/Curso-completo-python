# Entendendo dicionário

# Criando um dicionario vazio
lista_de_compra = {}

# Adicionando item no dicionário
lista_de_compra[1] = ('arroz')
lista_de_compra[2] = ('feijao')
lista_de_compra[3] = ('Macarronada')

# Alterando o item pela chave
lista_de_compra[1] = ("Peixe frito")

# pegando um item apenas do dicionário pela chave
print(lista_de_compra[2])

# Excluindo um item pela chave
del lista_de_compra[2]

#############################################

lista_de_compra_fruta = {
    1: "Maça",
    2: "Banana",
    3: "Peira",
    4: "Uva",
    5: "Abacaxi",
}

# Iterando sobre esse dicionario
for fruta in lista_de_compra_fruta:
    print(fruta, lista_de_compra_fruta[fruta])

# Adicionando na lista
lista_de_compra_fruta[6] = ('Melancia')

print(lista_de_compra)
print(lista_de_compra_fruta)