# O que é namespace?
#
# Namespace é uma estrutura de dados real que mapeia nomes para objetos. Cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. Sempre que você cria um nome, essa associação é guardada dentro de um
# namespace.


namespace_global = globals()
um_nome = "um_nome (GLOBAL)"

print(id(um_nome), id(namespace_global['um_nome']))

def func_global(sou_local: str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (local)"
    print("LOCAL (namespace da função)")
    print(locals())
    print()


# func_global("olá, mundo! (LOCAL)")
# print()


# print("GLOBALS (namespace do modulo)")
# for chave, valor in list(globals().items()):
#     print(f"{chave}: {valor}")
