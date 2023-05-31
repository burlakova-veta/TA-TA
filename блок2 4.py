import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,100))
print(a)
for j in range(len(a)):
    i=len(a)-1
    while i>0:
        if a[i]<a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
        i-=1
print(a)