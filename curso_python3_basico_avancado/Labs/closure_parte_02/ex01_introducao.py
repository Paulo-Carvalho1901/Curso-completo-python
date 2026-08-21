# Link para leitura sobre Closures
# https://realpython.com/python-closure/
# https://earthly-dev.translate.goog/blog/python-closures-decorators/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc
# 
# Closures em Python
#
# O que são closures?
# Closures ocorrem quando funções internas, definidas dentro de outras funções,
# referenciam variáveis livres do seu escopo. Variáveis livres são as
# variáveis que não foram definidas no escopo da função interna (são da função
# externa).
# Se a função externa retornar apenas a referência da função interna, então
# o interpretador precisará atrelar quaisquer referências a variáveis livres
# que a função interna precisar para que ela possa ser executada corretamente.
# São muito usados em programação funcional, decoradores de função e algoritmos
# em geral.

# A regra LEGB e como o Python a usa para resolver nomes
#
# O Python segue uma ordem específica e unidirecional para busca por nomes.
# A ordem sempre vai do escopo mais interno para o mais externo:
#
# Certo ✅: Local -> Enclosing -> Global -> Built-In -> ❌ NameError
# Errado ❌: Built-In -> ❌Global -> ❌Enclosing -> ❌Local
#
# De nenhum escopo externo é possível usar algo de escopo interno.

def externa(a):
    # Enclosing
    def interna(b):
        # Função interna precisa de `a`
        return f"{a} {b}"

    return interna  # Função interna não executada


imcompleto = externa("Paulo")
completo = imcompleto("Carvalho")

print(completo)
