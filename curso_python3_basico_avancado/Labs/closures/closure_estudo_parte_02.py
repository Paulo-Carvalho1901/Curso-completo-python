# Entendendo a função closure

def func():
    lista = []
    def func2(x):
        lista.append(x)
        return lista

    return func2


x = func()
print(x(10, 2))
