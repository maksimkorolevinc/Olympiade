n = int(input())
f = int(input())
ar = input()
ar = ar.split()
if f == 1:
    for i in range(len(ar)):
        ar[i] = int(ar[i])
    y = ar
    min = 10**10
    id = []
    for i in range(1, n+1):
        id.append(i)
    x = id
    mins  = []
    for j in range(n):
        ar = y
        id = x
        good = True
        ar = ar[-j:] + ar[:-j]
        id = id[-j:] + id[:-j]
        ar.append(ar[0])
        a = ar[1]
        for i in range(1, len(ar)):
            if a < ar[i]:
                good = False
                break
            a += 1
        if min > ar[1] and good:
            min = ar[1]
            b = [min, id[1]]
            mins.append(b)
    mins.sort()
    print(mins[0][0], mins[0][1])
else:
    min = 10**10
    for i in range(len(ar)):
        ar[i] = int(ar[i])
    m = ar[0]
    x,y,z = ar[1], ar[2], ar[3]
    pl = input()
    pl = pl.split()
    ids = []
    for i in range(1, n+1):
        ids.append(i)
    best = []
    for i in range(len(pl)):
        pl[i] = int(pl[i])
    copy = pl
    copid = ids
    for j in range(len(pl)):
        pl = copy
        ids = copid
        pl = pl[-j:] + pl[:-j]
        ids = ids[-j:] + ids[:-j]
        good = True
        while len(pl) < n:
            pl.append(0)
        for i in range(m, n):
            pl[i] = ((x*pl[i-2] + y*pl[i-1] + z)%(10**9) + 1)
        a = pl[n-1] - (n-1)
        for i in range(n):
            if a < pl[i]:
                good = False
                break
            a += 1
        if min > pl[n-1] - (n-1) and good:
            min = pl[n-1] - (n-1)
            print(min, ids[0])
            break

