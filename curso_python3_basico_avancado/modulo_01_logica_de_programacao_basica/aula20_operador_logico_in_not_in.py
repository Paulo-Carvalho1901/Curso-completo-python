# Operadores in e not in
# Strings são iteráveis

#  0 1 2 3 4 5 indices positivos
#  O t a v i o
# -6-5-4-3-2-1 indices negativos

nome = 'Otavio'
# print(nome[2])
# print(nome[-4])

# in - está em
print('a' in nome) # True
print('z' in nome) # False
print(25 *'-')
# not in - não está em
print('pau' not in nome) # True
print('vio' not in nome) # False

print(25 *'-')
nome_pessoal = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_pessoal:
    print(f'{encontrar} está em {nome_pessoal}')
else:
    print(f'{encontrar} não está em {nome_pessoal}')
