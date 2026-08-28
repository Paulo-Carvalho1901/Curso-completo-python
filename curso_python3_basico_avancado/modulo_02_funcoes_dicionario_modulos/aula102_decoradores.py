# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar sintatico)

# Função decorada
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar...')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Vou te mostrar seu resultado {resultado}')
        print('Ok, agora você foi decorada!')
        return resultado
    return interna


@criar_funcao
def inverter_string(string):
    # print(f'{inverter_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Paramatro deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverter_string)
invertida = inverter_string('123')
print(invertida)
