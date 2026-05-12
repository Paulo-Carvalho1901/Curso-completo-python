"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# print('Valor' if True else 'outro valor')
# print('Valor' if False else 'outro valor')

# Explicando de modo mais facil para entender operação ternária
# condicao = 20 == 21
# variavel = 'valor do if' if condicao else 'valor do else'
# print(f'A condiçao é: {condicao} o resultado é: {variavel}')

digito = 9 # condição > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
