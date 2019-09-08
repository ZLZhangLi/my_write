n = int(input())
m = list(map(int,input().strip().split()))

def f1(coins,amount):
    coins.sort()
    coins = coins[::-1]
    count = 0
    for i in range(len(coins)):
        count += amount // coins[i]
        amount %= coins[i]
    if amount == 0:
        res = count
    else:
        res = -1
    return res

def f2(coins, amount):
    coins.sort()
    dp = {0:0}
    for i in range(1,amount + 1):
        dp[i] = amount + 1
        for j in coins:
            if j <= i:
                dp[i]=min(dp[i],dp[i-j]+1)
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]
print(f1(m,n))
print(f2(m,n))