# Entendendo a função closure

def func():
    x = 0
    # variavel "x" enclosing, compartilhada com func2, possibilitando 
    # lembrar desse valor, e efetuando a closure
    def func2(x):
        x += 1
        return x 

    return func2


x = func()
print(x(2))
print(x(3))
print(x((3, 12)))
