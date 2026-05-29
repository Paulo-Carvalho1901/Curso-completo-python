# Clousure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def soudar(nome):
        return f'{saudacao}, {nome}!'
    return soudar # retornando a funçao em si para ela mesma


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia('Paulo')) # fazendo o fechamento da função (clousure)
# print(falar_boa_noite('Andreia'))

for nome in ['Paulo', 'Andreia', 'Davi']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
