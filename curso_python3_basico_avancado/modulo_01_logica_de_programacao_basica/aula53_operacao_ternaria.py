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

# movo digito recebe o valor do digito
# que novo caso é 9, se a condição do valor do digito for <= 9
# caso contrario o novo digito recebe 0
novo_digito = digito if digito <= 9 else 0

# novo digito 2 é = 0, caso a condição do valor do digito
# seja > 9 caso contrario o valor do digito recebe o valor dele mesmo que no
# caso é 9
novo_digito_2 = 0 if digito > 9 else digito
print(novo_digito)
print(novo_digito_2)
