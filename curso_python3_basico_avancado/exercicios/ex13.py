"""
Faça uma lista de compras com listas
o usúario deve ter a a possibilidade de 
inserir, apagar, e listar valores da sua lista
não permita que o programa quebre com
erros de indices inesistentes na lista
"""
lista = []

while True:
    print('Selecione uma opção.')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        print('i')
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        print('l')
    else:
        print('Por favor escolha i a ou l.')
