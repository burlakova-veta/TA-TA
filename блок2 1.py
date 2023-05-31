import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,50))
print(a)
for i in range(len(a)):
    min=a[i]
    k=i
    for j in range(i,len(a)):
        if min>a[j]:
            min=a[j]
            k=j
    a[i], a[k] = a[k], a[i]
print(a)