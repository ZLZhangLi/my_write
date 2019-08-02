N , M = list(map(int,input().strip().split()))
Ci = []
while len(Ci) != M:
    Ci = list(map(int,input().strip().split()))
Num1 = [0 for i in range(N)]
Di = sorted(Ci)
for j in range(M):
    for k in range(N):
        if Ci[j] == k + 1:
            Num1[k] += 1
        else:
            continue
print (min(Num1))