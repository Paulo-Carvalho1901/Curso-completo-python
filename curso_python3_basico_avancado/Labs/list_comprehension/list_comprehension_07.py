# for aninhado
for x in range(1, 11):
    for y in range(1, 6):
        print(x, y)

print()
# for aninhado com list comprehension

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x * 1000, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(linhas_e_colunas)
