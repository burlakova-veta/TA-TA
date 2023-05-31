import random
x = int(input())
y = int(input())
z = int(input())
count = 0
if (x / 2) % 2 == 1:
    count += 1
    print(x, '= 2 *', x/2)
if (y / 2) % 2 == 1:
    count += 1
    print(y, '= 2 *', y/2)
if (z / 2) % 2 == 1:
    count += 1
    print(z, '= 2 *', z/2)
print(count)