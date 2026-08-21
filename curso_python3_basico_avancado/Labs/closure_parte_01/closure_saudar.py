def criar_saudacao(nome):
    def saudar():
        print(f'Olá, {nome}')
    return saudar


saudar_paulo = criar_saudacao('Paulo')
saudar_paulo()