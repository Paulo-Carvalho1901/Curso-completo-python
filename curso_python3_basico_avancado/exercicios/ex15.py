# Exercícios com funções

# Crie um função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

"""
explicação
função recebe *args nome da funçao é multiplica
crio uma variável com total é 1 porque se fosse em zero
teria um problema pq todo numero * zero é zero.
depois faço um for em args e multiplico todos eles
e retorno o total acumulado dessa nultiplicação
"""

def multiplica(*args): 
    total = 1
    for numeros in args:
        total *= numeros
    return total


multiplica_1 = multiplica(2, 10, 2)
multiplica_2 = multiplica(1024, 10)
print(multiplica_1)
print(multiplica_2)

# Crie uma função fala se um número é par ou impar
# Retorne se o número é par ou impar

def par_impar(numero):
    if numero % 2 == 0:
        print(f'Seu numero foi {numero} é Par')
    else:
        print(f'Seu numero foi {numero} é impar')

par_impar(2)
