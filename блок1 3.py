import random
a=list()
n=20
for i in range(n):
    a.append(random.randint(0,30)-15)
print(a)
min = a[0]
for i in range(1, n):
    if a[i] < min:
        min = a[i]
print(min)