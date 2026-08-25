# Variáveis livres e nonlocal

print(globals())

# def fora(x):
#     a = x

#     def dentro():
#        # rint(locals())
#        # print(dentro.__code__.co_freevars)
#        return a
#     return dentro


# dentro = fora(10)
# dentro_2 = fora(20)

# print(dentro())
# print(dentro_2())
