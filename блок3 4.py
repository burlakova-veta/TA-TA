import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,300)-150)
print(a)
b=list()
for i in range(n):
    if a[i]<0:
        b.append(a[i])
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[i]<b[j]:
            b[i], b[j] = b[j], b[i]
print('Отрицательные элементы массива:', b)