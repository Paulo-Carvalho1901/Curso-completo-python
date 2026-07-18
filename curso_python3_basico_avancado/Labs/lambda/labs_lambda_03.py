# Expressões Lambda
# Funções "Anônimas" ou funções sem nome

# Ex:
# Digamos que você está avaliando o preço de um serviço
# e quer saber do imposto será cobrado sobre o serviço
# o imposto é correspondendo a 30% do valor produto

# preco = 1000

# def calcula_imposto(preco):
#     resultado = float((preco * 30) / 100) # calculo do imposto 
#     return resultado


# print(calcula_imposto(1000))


# x = float(input('Digite o valor: '))

# print()
# calc_imposto = lambda x: x * 0.3 # calculo do imposto 
# print(calc_imposto(x))


def calcular_imposto(preco):
    return preco * 0.3


precos = [100, 500, 10, 25]

imposto = list(map(calcular_imposto, precos))
print(imposto)

print()
imposto_2 = list(map(lambda x: x * 0.3, precos))
print(imposto_2)
