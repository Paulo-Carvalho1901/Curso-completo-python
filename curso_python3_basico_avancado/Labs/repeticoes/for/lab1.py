#       0123
nome = 'Davi'

tamanho_da_string = len(nome)
indice = 0

while indice < tamanho_da_string:
    print(nome[indice], indice)

    indice += 1

print()

nome_2 = 'Paulo'

for letra in nome_2:
    print(letra)
