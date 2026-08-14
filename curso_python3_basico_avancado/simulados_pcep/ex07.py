# What is the expected output of the following code ?

k = 1

for i in range(1,2):
    for j in range(-1,2):
        if i == j:
            k += 1
        else:
            break
print(k)