n = int(input())
ss = input()
m = list(map(int,input().strip().split()))
aa = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
bb = []
for index in range(len(ss)):
    bb.append(aa.index(ss[index]))
for i in bb:
    m[i] = 0
res = m.index(max(m))
print(aa[res])