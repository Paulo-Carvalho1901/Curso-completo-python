# Escopo e namespace dos modulos

"""Documentação com docstring"""

um_nome = 'um_nome (GLOBAL)'



print('Nome do modulo:', __name__)
print('Arquivo do modulo:', __file__)
print('Documentação do modulo:', __doc__)
print()

print('Fora da função:', um_nome)
