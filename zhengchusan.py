N, M = list(map(int,input().strip().split()))
count = 0
for i in range(N,M+1):
    if ((i * (i + 1)) / 2) % 3 == 0:
        count += 1
print (count)