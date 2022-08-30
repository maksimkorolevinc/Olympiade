n = int(input())
d = int(input())
a = []
for i in range(n):
    a.append(int(input()))
count = 0
max = a[0] // d + 1
for i in range(1, len(a)):
    if i + 1 <= max:
        count = a[i]//d + i + 1
        if count > max:
            max = count
    else:
        break
if max > len(a):
    max = len(a)
print(max)