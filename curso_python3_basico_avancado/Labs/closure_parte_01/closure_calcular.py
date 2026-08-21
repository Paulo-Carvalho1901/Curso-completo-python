# Capacidade de perceber o "enterno" Tem consciência 
# do local onde ela foi escrita. Além do escopó
# interno, ela percebe o que está ao seu redor.

# Consiste em retornar uma funçao que use internamente
# variaveis (ou nomes) da função que a define

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

dobro = multiplicar(2)
triplo = multiplicar(3)

print(dobro(4))
print(triplo(3))
