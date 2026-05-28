# Entendendo o código

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


# chamada de função
print(executa(saudacao, 'Bom dia', 'Andreia'))
print(executa(saudacao, 'Boa noite', 'Paulo'))
