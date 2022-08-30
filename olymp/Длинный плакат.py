n = input()
k = int(input())
n = list(n)
string = ''
for i in range(len(n)):
    n[i] = int(n[i])
i = 0
while i + k < len(n):
    maxnum = n[i]
    maxid = i
    for j in range(i+1, k + i + 1):
        if n[j] > maxnum:
            maxnum = n[j]
            maxid = j
    string += str(maxnum)
    k -= maxid - i
    i = maxid + 1
print(string)