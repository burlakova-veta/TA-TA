import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,10))
print(a)
for i in range(len(a)):
    min=a[i]
    for j in range(i,len(a)):
        if min>a[j]:
            min=a[j]
            k=j
            print(a)
    a[i], a[k] = a[k], a[i]
print(a)