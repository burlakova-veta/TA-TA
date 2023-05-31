import random
a=list()
n=int(input())
for i in range(n):
    a.append(random.randint(0,30)-15)
print(a)
for i in range(len(a)):
    if a[i]<0:
        
print(a)