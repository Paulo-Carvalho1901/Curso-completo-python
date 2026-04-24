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

# Valores mutáveis
#  Podem ser alterados após a criação, sem criar um novo objeto.

# Principais tipos mutáveis:
# list – listas
# dict – dicionários
# set – conjuntos

lista = [1, 2, 3]
lista.append(4) # altera a lista original
print(lista)

dicionario = {"nome": "Paulo"}
dicionario["idade"] = 30  # adiciona novo item
print(dicionario)
