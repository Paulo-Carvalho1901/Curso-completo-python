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
p1 = {
    'nome': 'Paulo',
    # 'sobrenome': 'Carvalho'
}

# print('get')
# print(p1['nome'])
# print(p1.get('nome', 'Não existe')) # se nome não existir retorna nome ou valor padrão definido.

print('=*' * 35)
# metodo pop apaga um item utilizandoa chave do diconario
# print('pop')
# nome = p1.pop('nome')
# print(nome)
# print(p1)

print('=*' * 35)
# print('pop item')
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

print('=*' * 35)
# print('update')
# atualizando o dict
# p1.update({
#     'nome': 'novo_valor',
#     'idade': 35
# })

# atualizando dict com parametros nomeados
# p1.update(nome='novo valor', sobrenome='outro_valor', idade=42)
# print(p1)
print()
tupla = (('nome', 'outro valor'), ('idade', 30))
lista = [['nome', 'outro valor'], ['idade', 30]]
p1.update(lista)
print(p1)
