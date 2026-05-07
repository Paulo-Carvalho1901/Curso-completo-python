"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta os espaços no inicio e fim da frase
"""

frase = '               Olha só que           , coisa interessante                 '
lista_de_frases = frase.split(',')

for i, frases in enumerate(lista_de_frases):
    lista_de_frases[i] = lista_de_frases[i].strip()

print(lista_de_frases)
