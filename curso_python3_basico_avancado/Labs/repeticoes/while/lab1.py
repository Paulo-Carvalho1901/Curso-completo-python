# while entendo como ele funciona
# Solicitando o nome ao úsuario
nome = input('Digite seu nome: ')

# setando o indice em zero
indice = 0

novo_nome = '' # criando uma variável vazia

# Aqui onde criamos a lógica 
# enqaunto o indice for menor que tamanho da letra (condição) então entre no laço.
# pegando a letra pela posição do indice letra, no caso indice iniciado em 0 = nome(indice)
# assim fazendo a acumulando as interações letra a letra no variável novo_nome
# por fim imprimindo o valor.

while indice < len(nome): # condição
    letra = nome[indice] # pegando a letra
    novo_nome += f'*{letra}' # acumulando

    indice += 1 # AQUI a incremento do indice

novo_nome += '*'
print(novo_nome) 
