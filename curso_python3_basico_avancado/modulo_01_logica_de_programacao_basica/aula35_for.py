# texto = 'texto'

# i = 0

# while i < len(texto):
#     print(texto[i], i)

#     i += 1


# senha_salva = '1234'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Digite a senha: ({repeticoes})x ')

#     repeticoes += 1

# print('Aquele laço pode ter repetições infinitas. Voce tentou.')

texto = 'texto'

novo_letra = ''
for letra in texto:
    novo_letra += f'*{letra}'
    print(letra)
print(novo_letra + '*')
