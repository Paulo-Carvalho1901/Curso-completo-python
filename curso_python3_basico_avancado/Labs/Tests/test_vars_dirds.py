# vamos usar `vars()` e `dir()` no mesmo código anterior e confirmar isso.
#
# `vars()`: retorna o atributo `__dict__` de um objeto, que é onde seus
#           atributos são armazenados. se chamada sem argumentos, `vars()` se
#           comporta exatamente como `locals()`, retornando o namespace local.
# `dir()`:  sem argumentos, `dir()` lista todos os nomes disponíveis no escopo
#           atual. com um objeto como argumento, tenta listar todos os nomes
#           acessíveis nele (como métodos e atributos). note que `dir()`
#           retorna apenas os nomes, não os objetos ou seus valores.


um_nome = "um_nome (GLObal)"


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"
    print("locals (nomespace da função)")
    print("dir", dir())
    print('vars', vars())


func_global("arg (LOCAL)")
print()


# print("glbals (namespace do módulo)")
# print("dir", dir())
# print("vars", vars())
