n = int(input())
a = []
for i in range(n, n**2 + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count <= 2:
        a.append(i)
print(a)