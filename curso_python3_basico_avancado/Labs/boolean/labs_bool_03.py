# Testes utilidade

entrada = input('[E]ntrada [S]aida: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Acesso negado!')
