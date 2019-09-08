c = int(input())
m = []
n = []
num = 0
res = []
for i in range(c):
    m.append(list(map(int,input().strip().split())))

for i in range(len(m)):
    n = m[i][1:]
    n.sort(reverse=True)
    while(n[2]>0):
        num += n[2]
        n[0] -= n[2]
        n[1] -= n[2]
        n[2] = 0
        n.sort(reverse=True)
    # for j in range(len(n) - 2):
    #     num += n[j]
    #     n[j + 1] -= n[j]
    #     n[j + 2] -= n[j]
    #     #n.sort()
    res.append(num)
    num = 0
for i in res:
    print(i)

