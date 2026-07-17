cadastro_pessoa = [
    {"nome": "Paulo", "sobrenome": "Carvalho", "idade": 36},
    {"nome": "Davi", "sobrenome": "Carvalho", "idade": 11},
    {"nome": "Andreia", "sobrenome": "Carvalho", "idade": 42},
]

# # função que organiza por nome
# def organiza(item):
#     return item['nome']

# # ordenando recebendo o nome da função
# cadastro_pessoa.sort(key=organiza)

# # Iterando na funçao e printando o item
# for item in cadastro_pessoa:
#     print(item)

##############################################################################
# Outra forma de ordenar mais agora com função lambda
# cadastro_pessoa.sort(key=lambda item: item['nome'])

# for item in cadastro_pessoa:
#     print(item)

###############################################################################
# Outra forma mais simplificada de lambda

def exibir(lista):
    for item in lista:
        print(item)
    print()
    

l1 = sorted(cadastro_pessoa, key=lambda item: item['nome'])
l2 = sorted(cadastro_pessoa, key=lambda item: item['sobrenome'])
l3 = sorted(cadastro_pessoa, key=lambda item: item['idade'])

exibir(l1)
exibir(l2)
exibir(l3)
