n = int(input('Введите диапазон: '))
pos = int(input('Введите номер: '))
a = []
for i in range(1,n):
    a.append(i)
print(a)
while len(a) != 1:
    if len(a) != 1:
        mid = len(a)//2
    if pos > a[mid]:
        a = a[mid:len(a)]
        print(a)
    if pos < a[mid]:
        a = a[0:mid]
        print(a)
    elif pos == a[mid]:
        a = [a[mid]]
        print(a)
    else:
        print(a)
        break