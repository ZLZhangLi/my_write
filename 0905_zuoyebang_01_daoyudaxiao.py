import sys
class Solution(object):
    nextStep = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    step = 0

    def maxAreaOfIsland(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.step = 0
                    self.dfs(grid, i, j)
                    res = max(res, self.step)

        return res

    def dfs(self, grid, x, y):

        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
            return
        grid[x][y] = -1
        self.step += 1
        for i in range(len(self.nextStep)):
            self.dfs(grid, x + self.nextStep[i][0], y + self.nextStep[i][1])

a = Solution()
m_gird = []
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break
    m_gird.append(list(map(int,line.split())))

print(a.maxAreaOfIsland(m_gird))