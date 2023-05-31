import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,30)-15)
print(a)
max = a[0]
k = 0
min = a[0]
c = 0
for i in range(n):
    if a[i] > max:
        max = a[i]
        k = i
    if min > a[i]:
        min = a[i]
        c = i
a[k], a[c] = a[c], a[k]
print(a)