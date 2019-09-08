n,k = list(map(int,input().strip().split()))
m = list(map(int,input().strip().split()))
s = []
minSum = 0
for i in range(k):
    minSum += m[i]
for i in range(len(m)-2):
    temp = minSum + m[i + k - 1] - m[i-1]
    if temp < minSum:
        minSum = temp
        res = i

print(res + 1)