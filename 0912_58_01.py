m = int(input())
n = int(input())
m_grid = []
for _ in range(m):
    m_grid.append(list(map(int,input().strip().split())))
# print(m_grid)
class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
a = Solution()
res = a.minPathSum(m_grid)
print(res)