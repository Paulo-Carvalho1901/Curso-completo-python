"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# print('Valor' if True else 'outro valor')
# print('Valor' if False else 'outro valor')

# Explicando de modo mais facil para entender operação ternária
condicao = 20 == 21
variavel = 'valor do if' if condicao else 'valor do else'
print(f'A condiçao é: {condicao} o resultado é: {variavel}')
