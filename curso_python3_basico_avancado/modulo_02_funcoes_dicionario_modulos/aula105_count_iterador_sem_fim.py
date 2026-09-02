# count é um iterador sem fim

from itertools import count

c1 = count()
r1 = range(10)

# print(next(c1))
# print(next(c1))
# print(next(c1))

print('c1', hasattr(c1, '__iter__')) # Iteravel
print('c1', hasattr(c1, '__next__')) # Iterator
print('ri', hasattr(r1, '__iter__')) # Iteravel
print('ri', hasattr(r1, '__next__')) # Iterator

print('Count')
for i in c1:
    if i > 100:
        break

    print(i)
