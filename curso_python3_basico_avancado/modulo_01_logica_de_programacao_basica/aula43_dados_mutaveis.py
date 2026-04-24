"""
Cuidados com dados mutáveis
= - copiando o valor (imutável)
= - aponta para o mesmo valor na memória (mutável)
"""

# name = 'Paulo'
# last_name = name
# name = 'Paulo Carvalho'
# print(name)
# print(last_name)

"""
Para deixa mais claro
quando o valor for imutavel você esta copiando o valor para outra variável

quando o valor for mutavel você apenas esta referenciando o valor na memória
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)
