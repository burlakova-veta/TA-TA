import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,30))
print(a)
for j in range(n):
    max = a[0]
    max = 0
    k = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]
            k = i
    a[k], a[n-1] = a[n-1], a[k]
    n -= 1
    print(a, max, k, n)