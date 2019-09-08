import sys
n = int(input())
m = int(input())
m_gird = []
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break
    m_gird.append(list(map(int,line.split())))

nextStep = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def find_jewelry(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                step = 0
                ans = dfs(grid, step, i, j)
    return ans

def dfs(grid, step, x, y):
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] == 0:
        return
    grid[x][y] = -1
    step += 1
    flag = 0
    for i in range(len(nextStep)):
        if grid[x + nextStep[i][0]][y + nextStep[i][1]] == 9:
            flag = 1
            break
        else:
            flag = dfs(grid, step, x + nextStep[i][0], y + nextStep[i][1])
    return flag

print(find_jewelry(m_gird))