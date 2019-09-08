n = int(input())
dist = list(map(int,input().strip().split()))
value = list(map(int,input().strip().split()))
l = len(dist)
for i in range(l):
    res = dist[i] + 2*l
    print(res)
