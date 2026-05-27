"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg

# Apontando com uma variável uma função
saudacao_2 = saudacao

# executando essa função salva na variável
v = saudacao_2('Bom dia!')
print(v)
