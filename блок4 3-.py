import random
n = 3
m = 4
a = [0]*n
sum = [0]*n
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0,100)
        sum[i] += a[i][j]
for i in range(n):
    for j in range(m):
        print('{:4d}'.format(a[i][j]), end='  ')
    print('|', sum[i])
    print()
print('- - - - - - - - - - - -')