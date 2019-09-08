n = int(input())
m = list(map(int,input().strip().split()))

class Solution:
    def numPermsDISequence(self, S ):
        le = len(S)
        dp = [[0]*(le+3) for _ in range(le+1)]
        dp[0][1] = 1
        for i in range(1,le+1):
            if S[i-1] == 1:
                for j in range(i+1,0,-1):
                    dp[i][j] = (dp[i-1][j]+dp[i][j+1])%1000000007
            else:
                for j in range(1,i+2):
                    dp[i][j] = (dp[i-1][j-1]+dp[i][j-1])%1000000007
        return sum(dp[-1])%1000000007

a = Solution()
print(a.numPermsDISequence(m))