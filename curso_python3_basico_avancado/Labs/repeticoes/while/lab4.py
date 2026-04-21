# Exercício 3

# Faça um programa que continue pedindo uma senha ao usuário 
# até que ele acerte. Quando acertar, exiba uma mensagem de sucesso.

senha_secreta = 1234
senha_digitada = int(input('Digite uma senha: '))
contador = 0

while senha_digitada != senha_secreta:
    contador += 1
    print(f'Senha incorreta, tente novamente!')
    senha_digitada = int(input('Digite uma senha: '))

print(f'Você levou {contador} vezes para acertar.')
print('Acesso permitido parabéns!')
