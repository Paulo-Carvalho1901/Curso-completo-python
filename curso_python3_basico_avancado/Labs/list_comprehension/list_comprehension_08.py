string = 'Paulo Carvalho'
numeros_de_letras = 3

nova_string = [
    string[indice:indice + numeros_de_letras] 
    for indice in range(0, len(string), numeros_de_letras)
]

print(nova_string)
