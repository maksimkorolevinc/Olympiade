n = int(input())
all = input()
all = all.split()
for j in range(len(all)):
    all[j] = int(all[j])
q = int(input())
for j in range(q):
    sum = 0
    com = input()
    com = com.split()
    for k in range(len(com)):
        com[k] = int(com[k])
    if com[0] == 1:
        all[com[1] - 1] = com[2]
        for k in range(len(all)):
            sum += all[k]
        print(sum)
    else:
        all = all[-com[1]:] + all[:-com[1]]
        for k in range(len(all)):
            sum += all[k]
        print(sum)