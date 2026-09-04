# sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa
# que leia o nome dos quadro alunos e mostre a
# ordem sorteada

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista_sorteados = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista_sorteados)

for aluno in lista_sorteados:
    print(aluno)
