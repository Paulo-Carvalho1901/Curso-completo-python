# Teste utilidade operador or

entrada = input('[E]ntrada [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Acesso negado!')

# senha = False or False or 0 or 'ABC' or True
# print(senha)

# senha = input('Senha') or 'Sem senha'
# print(senha)
