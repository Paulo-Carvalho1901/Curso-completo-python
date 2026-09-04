# um professor quer sortear um dos
# seus quadro alunos para apagar
# o quedro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo 
# o nome do escolhido.

import random


nome_dos_alunos = ['Amanda', 'Flavio', 'Pedro', 'Luiz']

sorteado = random.choice(nome_dos_alunos)
print(f'O nome do aluno escolhido foi {sorteado}')
