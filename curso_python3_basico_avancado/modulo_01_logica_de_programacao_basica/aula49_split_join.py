"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta os espaços no inicio e fim da frase
"""

frase = '               Olha só que           , coisa interessante                 '
lista_de_frases_cruas = frase.split(',')

listas_frases = []
for i, frases in enumerate(lista_de_frases_cruas):
    listas_frases.append(lista_de_frases_cruas[i].strip())

print(lista_de_frases_cruas)
print(listas_frases)
