import importlib

import aula99_modulo_importado_98

print(aula99_modulo_importado_98.variavel)

for i in range(10):
    importlib.reload(aula99_modulo_importado_98)
    print(i)

print('Fim')
