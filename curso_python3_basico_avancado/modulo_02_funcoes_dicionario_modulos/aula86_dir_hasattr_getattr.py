# dir, hasattr e getattr em Python
# dir
string = 'Paulo'

# print(string)
# print(dir(string)) # tras todos os metosos disponiveis para uso

##############################################################################
# hasttr
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())
    print()

##############################################################################
# getattr
metodo = 'upper1'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)
