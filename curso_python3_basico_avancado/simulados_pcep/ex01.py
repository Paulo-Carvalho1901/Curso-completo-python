# What is the expected result of the following code ?
names = (True, False, True, False)
newnames = names[2:]

i = 0

for name in newnames[-1:]:
    if name:
         i += 1
print(i)
