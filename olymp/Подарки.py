n = int(input())
a = int(input())
b = int(input())
c = 0
while b != 0:
    k = n
    while k > 3 and b != 0:
        k -= 3
        b -= 1
    a -= n - k
    c += 1
while a > 0:
    a -= n
    c += 1
print(c)


