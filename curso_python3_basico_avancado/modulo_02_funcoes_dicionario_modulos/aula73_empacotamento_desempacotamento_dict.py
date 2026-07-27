# Empacotamento de desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Paulo',
#     'sobrenome': 'Carvalho'
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Carvalho'
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoas}
# print(pessoa_completa)

# args  e kwargs
# args (argumentos não nomeados)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(1, 2, 3, nome='Paulo', sobrenom='Roberto', idade=37, blabla='Qualquer coisa')
mostro_argumentos_nomeados(55, 99, 100,**pessoa_completa)

confi = {
    'arg1': 1, 
    'arg2': 2, 
    'arg3': 3, 
    'arg4': 4, 
}

mostro_argumentos_nomeados(**confi)
