import random
n = 3
m = 4
a = [0]*n
b = [0]*n
for i in range(n):
    a[i] = [0] * m
max = 0
i = -1
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0,100)
        if max < a[i][j]:
            max = a[i][j]
            ik = i
for i in range(n):
    for j in range(m):
        print('{:4d}'.format(a[i][j]), end='  ')
    print()
print('Строка с максимальным элементом -', ik + 1)
sum = a[ik][0]
for j in range(1,m):
    sum += a[ik][j]
print('Сумма элементов строки:', sum)