# args - argumentos não nomeados
# kwargs - argumentos nomeados

# * trabalha com uma sequência de valores (tuple, lista, etc.)
# ** trabalha com pares chave-valor (dict)

# EMPACOTANDO EM UM DICT
# def empacote(**kwargs):
#     print(kwargs)

# pessoa = empacote(nome='Paulo', sobrenome='Roberto', idade=17)


########################################################################
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADO', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Paulo', sobrenome='Carvalho')
