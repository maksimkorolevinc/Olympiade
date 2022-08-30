n = int(input())
k = int(input())
a = [['x' for i in range(n//k)] for j in range(n//k)]
for i in range(len(a)):
    print(a[i])
s = 0
for i in range(len(a)):
    s += (len(a) - 1)*2
if n == k:
    print(0)
else:
    print(s)
