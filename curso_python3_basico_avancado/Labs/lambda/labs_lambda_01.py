cadastro_pessoa = [
    {"nome": "Paulo", "sobrenome": "Carvalho", "idade": 36},
    {"nome": "Davi", "sobrenome": "Carvalho", "idade": 11},
    {"nome": "Andreia", "sobrenome": "Carvalho", "idade": 42},
]

# função que organiza por nome
def organiza(item):
    return item['nome']

# ordenando recebendo o nome da função
cadastro_pessoa.sort(key=organiza)

# Iterando na funçao e printando o item
for item in cadastro_pessoa:
    print(item)
