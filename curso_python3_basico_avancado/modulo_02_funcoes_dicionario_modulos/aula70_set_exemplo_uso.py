# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÈNS VOCE ACERTOU!')
        break

    print(letras)
