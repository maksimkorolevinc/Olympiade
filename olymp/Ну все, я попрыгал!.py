x = int(input())
y = int(input())
n = int(input())
a = []
sum = 0
count = 0
while sum < n:
    sum += y
    count += 1
    if sum >= n:
        break
    sum += x
    count += 1
    if sum >= n:
        break
while sum != n:
    sum -= y
    sum += x
    if sum == n:
        break
print(count)