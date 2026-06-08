# Escopo e namespace dos modulos

"""Documentação com docstring"""


# nome definido no escopo global (modulo)
um_nome = 'um_nome (GLOBAL)'


# nome definido no escopo global (modulo)
def func_global(sou_local: str) -> None:
    # Escopo local (funções e seus parametros)

    # um_nome no escopo local é OUTRA VARIÁVEL (sem relação outro escopo)
    um_nome = "um_nome (LOCAL)" # nome definido no escopo local
    outro_nome = "outro_nome (LOCAL)" # nome definido no escopo local

    # Parâmetros de funções também são do escopo local da função
    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")


# Nomes de dentro da função não estão DISPONÍVEL fora da função
# NÃO FUNCIONARÁ
# print(outro_nome, sou_local)


print('Nome do modulo:', __name__)
print('Arquivo do modulo:', __file__)
print('Documentação do modulo:', __doc__)
print()

func_global("Olá mundo: (LOCAL)")
# Saída: Dentro da função: um_nome (LOCAL), outro_nome (LOCAL), arg (LOCAL)

print('Fora da função:', um_nome) # Escopo GLOBAL
