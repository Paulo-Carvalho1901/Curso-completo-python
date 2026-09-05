"""
Escreva um programa que faça o 
computador "PENSAR" em um número inteiro
entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela
se o usuário venceu ou pedeu
"""

from random import randint

escolha_computador = randint(0, 5)

numero_escolhido = int(input('Digite um némero de 1 a 5: '))

if escolha_computador == numero_escolhido:
    print('Parabéns voce ganhou!')
else:
    print('Sorry try again!')
