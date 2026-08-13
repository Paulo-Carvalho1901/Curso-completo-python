# Which of the approachable except branches is taken into consideration when an exception occurs?
# Qual dos blocos except aplicáveis é considerado quando uma exceção ocorre?

"""
last matching branch 
Último bloco correspondente

Any of the matching branches
Qualquer um dos blocos correspondentes

First matching branch
Primeiro bloco correspondente

Em Python, quando uma exceção ocorre, os blocos except são 
avaliados de cima para baixo. O primeiro except compatível 
com a exceção lançada é executado, e os demais são ignorados.

"""
try:
    x = int("abc")
except ValueError:
    print("ValueError tratado")
except Exception:
    print("Exception genérica")
