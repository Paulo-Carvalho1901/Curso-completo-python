# Uma empresa decidiu da um bônus
# de 100% sobre o faturamento total
# para a equipe de vendas, objetivo: calcular
# o valor do bunus e o faturamento final da empresa
# após substituir esse bõnus.

# Faturamento inicial: 50.000
# Percentual do bônus 0.10

faturamento = 50000
percentual_bonus = 0.1

bonus_total = faturamento * percentual_bonus
faturamento_liquido = faturamento - bonus_total

print(f'Faturamento liquido', faturamento_liquido)
print(f'Bônus total', bonus_total)
