"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Eles podem receber valores específicos.
Por padrão, funções Python retornam None (nada).
"""

# Criando uma função
# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c): # parâmetro
#     print(a, b, c) # utilizando os valores

# imprimir(1, 2, 3) # argumento (valores)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Maria')
saudacao('João')
saudacao()
