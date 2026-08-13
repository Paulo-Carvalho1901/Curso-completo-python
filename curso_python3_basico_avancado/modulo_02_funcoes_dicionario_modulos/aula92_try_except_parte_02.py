# Try, except, else, and finally

try:
    a = 10
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('variável b não está definida.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Mensagem', error)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR...')