n = int(input())
dp = [[0 for _ in range(52)] for _ in range(n)]
x = [int(x) for x in input().split()]
for i in range(n):
    for j in range(1,x[i]+1):
        dp[i][j] = j / x[i]
    for j in range(x[i]+1,52):
        dp[i][j] = 1
res = [0]*52
for i in range(1,52):
    tmp = 1
    for j in range(n):
        tmp *= dp[j][i]
    res[i] = tmp
tmp = 0
for i in range(1,52):
    if res[i] > 0:
        tmp += i * (res[i] - res[i - 1])
print(":.2f".format(tmp))