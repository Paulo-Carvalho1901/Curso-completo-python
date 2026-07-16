# Operação ternaria
# Sintaxe

# valor_se_verdadeiro if condicao else valor_se_falso

# Comparando com um if normal

idade = 20
if idade >= 18:
    status = 'Maior de idade'
else:
    status = 'Menor de idade'
print(status)

# Operação ternária
idade = 20
status = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(status)