ll = list(map(int,input().strip().split()))
def PredictTheWinner2(nums):
    m = 0
    M = 0
    while (nums):
        a = max(nums[0], nums[-1])
        m += a
        nums.remove(a)
        if nums:
            b = max(nums[0], nums[-1])
            M += b
            nums.remove(b)
    if M > m:
        print('No')
    else:
        print('Yes')

def PredictTheWinner(nums):
    n = len(nums)
    if n % 2 == 0 or n == 1:
        return True
    dp = [[0] * n for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

    return dp[0][-1] >= 0

if __name__ == '__main__':
    res = PredictTheWinner(ll)
    if res:
        print('Yes')
    else:
        print('No')
    PredictTheWinner2(ll)