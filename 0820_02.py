import time
n = int(input())
res = [0 for i in range(n+1)]
start = time.clock()
for i in range(2,n+1):
    if (i & 1) == 0:
        res[i] = res[int(i / 2)] + 1
    else:
        res[i] = min(res[int((i+1) / 2)], res[int((i-1) / 2)]) + 2
end = time.clock()
print(res[n])
print(end-start)

