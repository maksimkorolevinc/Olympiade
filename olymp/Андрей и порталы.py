s = int(input())
e = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = 0
t = 0
min = 10**8
for i in range(len(a)):
    if min > a[i]:
        min = a[i]
    if max < a[i] and a[i] < e and max < e:
        max = a[i]
t += abs(s - min)
t += abs(max - 1 - e)
print(t)