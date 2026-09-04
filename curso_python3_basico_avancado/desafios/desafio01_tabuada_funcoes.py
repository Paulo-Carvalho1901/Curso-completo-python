"""
Faça uma função que leia um número
inteiro qualquer e mostre na tela
a sua tabuada completa.
"""

def tabuada(numero):
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

