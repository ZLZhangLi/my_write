# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#
#         # If the starting cell has an obstacle, then simply return as there would be
#         # no paths to the destination.
#         if obstacleGrid[0][0] == 1:
#             return 0
#
#         # Number of ways of reaching the starting cell = 1.
#         obstacleGrid[0][0] = 1
#
#         # Filling the values for the first column
#         for i in range(1,m):
#             obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
#
#         # Filling the values for the first row
#         for j in range(1, n):
#             obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
#
#         # Starting from cell(1,1) fill up the values
#         # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
#         # i.e. From above and left.
#         for i in range(1,m):
#             for j in range(1,n):
#                 if obstacleGrid[i][j] == 0:
#                     obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
#                 else:
#                     obstacleGrid[i][j] = 0
#
#         # Return value stored in rightmost bottommost cell. That is the destination.
#         return obstacleGrid[m-1][n-1]
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        动态规划（自底向上）
        """
        # m代表格子的列数，n代表格子的行数
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        # 创建一个数组r 用于保存所有子问题的解
        r = [[0] * m for _ in range(n)]
        # 一行一行构建从起点[0,0]到点[i,j]的路径数
        for i in range(0, n):
            for j in range(0, m):
                # 如果[i,j]是障碍物，则r[i][j]=0
                if obstacleGrid[i][j] == 1:
                    r[i][j] = 0
                # 如果[i,j]是起点，则r[i][j]=1
                elif i == 0 and j == 0:
                    r[i][j] = 1
                else:
                    # 因为机器人只能往下或者往右移动
                    # 得到动态方程，如下
                    #     r[i][j] = r[i-1][j] + r[i][j-1] （i>1,j>1）
                    #     且当i=0时，r[i][j] = r[i][j-1]
                    #       当j=0时，r[i][j] = r[i-1][j]
                    if i == 0:
                        r[i][j] = r[i][j - 1]
                    elif j == 0:
                        r[i][j] = r[i - 1][j]
                    else:
                        r[i][j] = r[i - 1][j] + r[i][j - 1]

        return r[n - 1][m - 1]

n,m,k = list(map(int,input().strip().split()))
juzhen = []
for i in range(n):
    juzhen.append([])
    for j in range(m):
        juzhen[i].append(0)
#r = [[0] * m for _ in range(n)]
for _ in range(k):
    i,j = list(map(int,input().strip().split()))
    juzhen[i][j] = 1

a = Solution()
res = a.uniquePathsWithObstacles(juzhen)
print(res)