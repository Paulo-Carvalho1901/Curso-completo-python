"""
(Ex13) da lista de exercicios

Faça uma lista de compras com listas
o usúario deve ter a a possibilidade de 
inserir, apagar, e listar valores da sua lista
não permita que o programa quebre com
erros de indices inesistentes na lista
"""

lista_de_compras = []


while True:
    print('Selecione uma opção: ')
    opcao = input('Digite apenas [I]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista_de_compras.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha uma indice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Digitar apenas números inteiros.')
        except IndexError:
            print('Indice não existe para ser apagado.')
    elif opcao == 'l':
        if len(lista_de_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
    else:
        print('Por favor digite apenas i, a e l.')