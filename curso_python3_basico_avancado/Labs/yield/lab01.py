# Criando um lógica para praticar

def generator(n=0, max=10):
    while True:
        yield n

        if n > max:
            return
        n += 1


gen =  generator()
for n in gen:
    print(n)
