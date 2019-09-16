# n,b,s = list(map(int,input().strip().split()))
# pi,vi = [], []
# for _ in range(n):
#     a,b = list(map(int,input().strip().split()))
#     pi.append(a)
#     vi.append(b)
#
# print(str(200) + ' ' + str(5) + ' ' +str(1))

N, V, M = list(map(int, input().strip().split()))
p,v = [],[]
f = [[0  for i in range(M+1)]for j in range(V+1)]
def ZeroOnePack(cost, mass, worth, n, m):
    for i in range(n, cost-1, -1):
        for j in range(m, mass-1, -1):
            f[i][j] = max(f[i][j], f[i-cost][j-mass] + worth)
for i in range(N):
    #v, m, w = (int(i) for i in input().split())
    pi, vi = list(map(int, input().strip().split()))
    p.append(pi)
    v.append(vi)
    ZeroOnePack(pi, 1, vi, V, M)
# print(f[-1][-1])
s1 = f[-1][-1]
m_index = v.index(f[-1][-1])
s2 = p[m_index]
s3 = M
print(str(s1) + ' ' + str(s2) + ' ' +str(s3))