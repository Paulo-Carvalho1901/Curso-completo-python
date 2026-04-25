# Itere com o laço for em uma lista de nomes
# e exiba o nome e o indice na saída

lista_nomes = ['Paulo', 'Andreia', 'Davi']

# pego o tamaho da minha lista e pego range do tamanho da lista
# assim terei os indices de cada iteração
indices  =  range(len(lista_nomes))


for i in indices:
    print(i, lista_nomes[i], type(lista_nomes[i]))
