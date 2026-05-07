"""
Faça uma lista de compras com listas
o usúario deve ter a a possibilidade de 
inserir, apagar, e listar valores da sua lista
não permita que o programa quebre com
erros de indices inesistentes na lista
"""
import os

lista = []

while True:
    print('Selecione uma opção.')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        """
        Limpa o terminal
        solicita um valor ao usuário
        da uma append na lista do valor solicitado
        """
        os.system('clear') 
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        # Solicitando um indice da lista
        indice_str = input(
            'Escolha um indice para apagar: '
        )

        # Tratamento de erros possiveis do programa
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite números int.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        # limpa o terminal
        os.system('clear')

        # Valida se à algo para lista
        if len(lista) == 0:
            print('Nada para listar.')
            
        # Itera sobre a lista mostrando seu indice e valor
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor escolha i a ou l.')
