# Imprecisão de ponto flutuante
# 

numero_1 = 0.1
numero_2 = 0.2

soma = numero_1 + numero_2
print(soma)

# Os Os floats modernos seguem o padrão: IEEE 754

# Ele define como números de ponto flutuante são armazenados.
# Um float possui:
# Sinal
# Expoente
# Mantissa (fração)

# Isso permite armazenar números muito grandes e muito pequenos.

# Exemplo

print(0.1 + 0.2)
print(0.1 + 0.1 + 0.1)
print(1.1 + 2.2)

# Exemplos mais praticos

x = 0.1 + 0.2
print(x == 0.3)

# Por que é perigoso?
# Imagine um sistema bancário:

saldo = 0.1 + 0.2
if saldo == 0.3:
    print('OK')
else:
    print('Erro')


# Formas de contornar

resultado = round(0.1 + 0.2, 2)
print(resultado)

# Exemplo

x = round(0.1 + 0.2, 2)
print(x == 0.3)
