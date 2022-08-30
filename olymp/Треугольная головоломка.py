t = int(input())
n = int(input())
all = []
for i in range(n):
    tr = input()
    tr = tr.split()
    for j in range(len(tr)):
        tr[j] = int(tr[j])
    tr.append(tr[0])
    tr.append(tr[1])
    all.append(tr)
lenths = []
for i in range(n):
    side = []
    for j in range(len(all[i])-2):
        if j == 0 or j%2 == 0:
            side.append(((all[i][j+2] - all[i][j])**2 + (all[i][j+3] - all[i][j+1])**2)**(1/2))
    lenths.append(side)
for i in range(len(lenths)):
    lenths[i].sort()
    print(lenths[i])
"""for i in range(len(lenths)):
    lenths[i].append(i+1)
    lenths[i].reverse()
sum = []
for i in range(len(lenths)):
    sum += lenths[i]
for i in range(len(sum)):
    if i != 0 and i%4 != 0:
        x = sum[i]
        for j in range(i+1, len(sum)):
            if x == sum[j]:
                for k in range(len(lenths)):
                    if x in lenths[k]:"""
for i in range(len(lenths)):
    for j in range(len(lenths[i])):
        x = lenths[i][j]
        for k in range(len(lenths)):
            if lenths[k] != lenths[i]:
                if x in lenths[k]: