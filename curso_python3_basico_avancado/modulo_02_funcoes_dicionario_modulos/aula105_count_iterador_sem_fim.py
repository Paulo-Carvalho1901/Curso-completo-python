# count é um iterador sem fim

from itertools import count

c1 = count(10)
r1 = range(10, 50)

# print(next(c1))
# print(next(c1))
# print(next(c1))

print('c1', hasattr(c1, '__iter__')) # Iteravel
print('c1', hasattr(c1, '__next__')) # Iterator
print('ri', hasattr(r1, '__iter__')) # Iteravel
print('ri', hasattr(r1, '__next__')) # Iterator

print() 
print('Count')
for i in c1:
    if i > 25:
        break

    print(i)

print()
print('Range')
for i in r1:
    print(i)
