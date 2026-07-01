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
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 45,
}

# print(len(pessoa)) # Len retorna quantidade de chaves de um dicionario
# print(pessoa.keys()) # pegando apenas as chaves
# print(pessoa.values()) # pega apenas o valor do dict
# print(pessoa.items()) # pega chave e valor do dict
pessoa.setdefault('idade', 35)
print(pessoa['idade'])

for chave, valor in pessoa.items():
    print(chave, valor)
