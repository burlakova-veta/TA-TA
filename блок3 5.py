import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,300))
print(a)
b=list()
for i in range(n):
    if i%2==0:
        b.append(a[i])
print('Элементы с четным индексом:', b)