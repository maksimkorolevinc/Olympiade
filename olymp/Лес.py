a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = int(input())
map = [['o' for i in range(2*k+1)] for j in range(2*k + 1)]
for i in range(len(map)):
    print(map[i])
x = len(map)//2
y = x
count = 0
completed = False
while True:
    for i in range(a):
        count += 1
        y += 1
        if y == len(map):
            completed = True
            break
    if completed:
        break
    for i in range(b):
        count += 1
        x += 1
        if x == len(map):
            completed = True
            break
    if completed:
        break
    for i in range(c):
        count += 1
        y -= 1
        if y == 0:
            completed = True
            break
    if completed:
        break
    for i in range(d):
        count += 1
        x -= 1
        if x == 0:
            completed = True
            break
    if completed:
        break
print(count)
