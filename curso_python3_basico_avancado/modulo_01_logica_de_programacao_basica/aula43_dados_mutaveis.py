"""
Cuidados com dados mutáveis
= - copiando o valor (imutável)
= - aponta para o mesmo valor na memória (mutável)
"""

name = 'Paulo'
last_name = name
name = 'Paulo Carvalho'
print(name)
print(last_name)

