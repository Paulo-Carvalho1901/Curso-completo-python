"""
Repetições
while (enquanto)
Executa uma ação enquanto a condiçao for verdadeira
Loope infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1 # controlador do código - incrementa

    # pulando o laço ele ignora e pula para proximo valor.
    if contador == 6:
        print('Não vou mostrar o', contador)
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostra o', contador)
        continue

    print(contador)
    # Quebrando o laço
    if contador == 40:
        break

print('Fim...')
