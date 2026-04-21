"""
Flag (Bandeira) - Marca um local
None = Não Valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None 

if condicao:
    passou_no_if = True # Bandeira
    print('Faça algo')
else:
    print('Não Faça algo')

# print(passou_no_if, passou_no_if is None) # checa se passou_no_if é None
# print(passou_no_if, passou_no_if is not None) # checa se passou_no_if não é None

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
