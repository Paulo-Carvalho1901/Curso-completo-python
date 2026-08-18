from sys import path

import aula100_package.modulo
from aula100_package.modulo import soma_do_modulo

# print(*path, sep='\n')

print(soma_do_modulo(2, 3))
print(aula100_package.modulo.soma_do_modulo(2, 3))
