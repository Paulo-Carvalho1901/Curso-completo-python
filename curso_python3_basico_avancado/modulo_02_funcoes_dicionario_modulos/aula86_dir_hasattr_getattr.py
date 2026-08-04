# dir, hasattr e getattr em Python

string = 'Paulo'

# print(string)
# print(dir(string)) # tras todos os metosos disponiveis para uso

##############################################################################

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())
