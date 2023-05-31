import random
n = 3
m = 4
a = [0]*n
b = [0]*n
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0,100)
for i in range(n):
    for j in range(m):
        print('{:4d}'.format(a[i][j]), end='  ')
    print()
print('----------------------')
for i in range(n-1):
    if a[i][0] > a[i+1][0]:
        for j in range(m):
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
for i in range(n):
    for j in range(m):
        print('{:4d}'.format(a[i][j]), end='  ')
    print()