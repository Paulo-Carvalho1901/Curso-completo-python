# Variáveis livres e nonlocal

def fora(x):
    a = x

    def dentro():
        return a
    return dentro


dentro = fora(10)
dentro_2 = fora(20)

print(dentro())
print(dentro_2())
