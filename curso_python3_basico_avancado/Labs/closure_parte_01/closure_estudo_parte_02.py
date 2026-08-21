# Entendendo a função closure

def func():
    y = 0
    # variavel "x" enclosing, compartilhada com func2, possibilitando 
    # lembrar desse valor, e efetuando a closure
    def func2():
        nonlocal y # O nonlocal serve para modificar uma variável do escopo enclosing.
        y += 1
        return y

    return func2


x = func()
print(x())
print(x())
print(x())
print()
h = func()
print(h())