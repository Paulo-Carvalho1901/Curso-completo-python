# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula100_package.modulo
# from aula100_package.modulo import soma_do_modulo
# from aula100_package import modulo

# # Má pratica de importação
# from aula100_package.modulo import *

# # print(*path, sep='\n')

# print(soma_do_modulo(2, 3))
# print(aula100_package.modulo.soma_do_modulo(2, 3))
# print(modulo.soma_do_modulo(2, 3))
# print(variavel)
# print(nova_variavel)

# from aula100_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from aula100_package import soma_do_modulo, fala_oi, variavel, nova_variavel

print(soma_do_modulo(2, 3))
fala_oi()
