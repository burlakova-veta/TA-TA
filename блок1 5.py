import random
a=list()
n=20
for i in range(n):
    a.append(random.randint(0,30))
print(a)
sum = 0
for i in range(n):
    if a[i] % 2 == 1:
        sum += a[i]
print(sum)