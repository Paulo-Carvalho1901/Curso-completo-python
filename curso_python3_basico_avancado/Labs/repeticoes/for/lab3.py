# Peça ao usuário para digitar **5 números** e mostre a soma no final.

soma = 0

for numero in range(1, 6):
    entrada = int(input('Digite um número: '))

    soma += entrada
print('A soma dos resultados é:', soma)
