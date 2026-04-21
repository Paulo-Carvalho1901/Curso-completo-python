"""
Faça um programa que peça o primero nome do úsuario. Se o nome tiver 4 letras ou
menos escreveu "Seu nome é curto; se tiver entre 5 e 6 letras, escreva
"seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite um nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
