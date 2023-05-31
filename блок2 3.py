import random
t=list()
n=int(input())
for i in range(n):
    t.append(random.randint(0,400))
t.sort()
print(t)
x=int(input())
t.append(x)
i=len(t)-1
while i>0:
    if t[i]<t[i-1]:
        t[i], t[i-1] = t[i-1], t[i]
    i-=1
print(t)