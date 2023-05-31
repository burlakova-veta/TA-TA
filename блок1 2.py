n = int(input())
s = len(str(n))
print(s)
k = n // 10 ** (s-1)
c = n % 10
n = n % 10 ** (s-1) + c * 10**(s-1) - c + k
print(n)