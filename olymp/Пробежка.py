a = int(input())
b = int(input())
sum = a - b
c = 1
while sum >= 0:
    b += 1
    if a - b > 0:
        sum += a - b
        c += 1
    elif a - b < 0:
        sum -= abs(a - b)
        c += 1
    else:
        c += 1
print(c)
