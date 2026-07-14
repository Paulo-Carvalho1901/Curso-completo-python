# Entendendo um pouco mais sobre boolean

# True == 1
# False == 0

print(100 * False)
print(100 * True)

print()
print(isinstance(True, bool))
print(isinstance(True, int))

print() # Varificando endereço na memória
print(id(hex(True)))
print(id(hex(1)))

print() # algumas exemplos
a = 1
b = 0

if b:
    if a/b > 2:
        print(id(hex(True)))
