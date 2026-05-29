# Clousure e funções que retornam outras funções

def criar_saudacao(saudacao, nome):
    def soudar():
        return f'{saudacao}, {nome}!'
    return soudar # retornando a funçao em si para ela mesma


saudacao_1 = criar_saudacao('Bom dia', 'Paulo')
saudacao_2 = criar_saudacao('Boa noite', 'Paulo')

print(saudacao_1)
print(saudacao_2)