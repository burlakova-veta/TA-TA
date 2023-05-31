import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,300)-150)
print(a)
c = a[-1]
for i in range(len(a)):
    if a[i]<0:
        k = i
        break
m = len(a) - 1
while m > k:
    a[m] = a[m-1]
    m -= 1
a[k+1] = c
print(a)