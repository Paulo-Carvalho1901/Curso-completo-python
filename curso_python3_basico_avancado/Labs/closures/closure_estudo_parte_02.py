# Entendendo a função closure

def func():
    lista = [] 
    # variavel "lista" enclosing, compartilhada com func2, possibilitando 
    # lembrar desse valor, e efetuando a closure
    def func2(x):
        lista.append(x)
        return lista

    return func2


x = func()
print(x(2))
print(x(3))
print(x((3, 12)))
