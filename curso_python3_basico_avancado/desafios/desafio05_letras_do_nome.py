"""
Crie um programa que leia o nome
completo de uma pessoa e mostre:
O nome com todas as letras minusculas
O nome com todas as letras maisculas
Quantas letras ao todo sem considerar os espaços
Quantas letras tem o primeiro nome
"""

nome_completo = input('Digite seu nome: ')

print(f'Seu nome com todas as letras é: {nome_completo}')
print(f'Seu nome com as letras minusculas é {nome_completo.lower()}')
print(f'Seu nome com as letras maiusculas é {nome_completo.upper()}')
nome_sem_espaço = nome_completo.replace(" ", "")
print(f'No seu {nome_completo} tem {len(nome_sem_espaço)} letras')
primeiro_nome = nome_completo.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')
