q = int(input())
w = int(input())
if q == 1:
    print(q)
else:
    if q == w:
        print(-1)
    else:
        if w - q == 1:
            print(q * (w - 1))
        else:
            if w < q*2 - 1:
                print(q*2)
            else:
                if w >= q*2 - 1:
                    print(q)
                else:
                    print(-1)