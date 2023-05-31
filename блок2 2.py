import random
b=list()
n=int(input())
for i in range(n):
    b.append(random.randint(0,30))
print(b)
for i in range(n):
    for j in range(n-1):
        if b[j]>b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print(b)