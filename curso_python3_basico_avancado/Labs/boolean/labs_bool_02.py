# Os operadores and e or usam short-circuit evaluation 
# (avaliação de curto-circuito), também chamada de 
# avaliação preguiçosa (lazy).

# A ideia é simples: o Python para de avaliar a expressão assim 
# que já consegue determinar o resultado.

# Operador and
# Para A and B:
# Se A for False, o resultado já será False.
# Não há necessidade de avaliar B.

x = False

if x and print("Executou"):
    pass
print("Fim")

# O print("Executou") nunca roda porque o Python viu que x é False.