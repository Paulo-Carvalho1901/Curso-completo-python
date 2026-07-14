# Documentação Python Sobre o assunto
# https://docs.python.org/pt-br/3.10/library/decimal.html

# Exemplo comun

# isclose, testa se o número estão proximos dos valores
from math import isclose

x = 0.1 + 0.1 + 0.1
y = 0.30005


print(isclose(x, y, abs_tol=0.004)) # tolerância absoluta
