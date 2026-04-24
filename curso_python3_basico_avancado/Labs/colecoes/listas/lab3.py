# Mutáveis e imutáveis

# Valores mutáveis
# Não podem ser alterados depois de criados.
# Se você “mudar”, na verdade cria um novo objeto.

# Principais tipos imutáveis:
# int – números inteiros
# float – números decimais
# complex – números complexos
# bool – True ou False
# str – strings (textos)
# tuple – tuplas
# frozenset – conjunto imutável

x = 10
x = x + 5 # cria um novo valor, não altera o 10 original
print(x)

texto = "Olá"
# texto[0] = "o"  ❌ ERRO: string é imutável
