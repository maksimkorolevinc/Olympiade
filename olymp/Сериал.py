n = int(input())
a = [int(input()) for i in range(n)]
id = [i for i in range(1, n+1)]
for i in range(n):
    b = []
    b.append(a[i])
    b.append(id[i])
    a[i] = b
a.sort()
c = 0
counts = []
for i in range(len(a)-1):
    if a[i][0] == a[i+1][0]:
        counts.append(1)
sum = 0
for i in range(len(counts)):
    sum += counts[i]
if n - sum > 2:
    for i in range(3):
        print(a[i][1])
else:
    print(0)