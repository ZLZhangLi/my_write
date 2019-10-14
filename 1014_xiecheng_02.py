m,n = list(map(int,input().strip().split()))
data = []
for _ in range(m):
    data.append(list(map(int,input().strip().split())))

def spiralOrder(matrix):
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []
    x, y = 0, 0
    cnt = 1
    state = "right"
    res = list()
    while (cnt <= m * n):
        # print x, y,state
        res.append(matrix[x][y])
        matrix[x][y] = -999999  # 标记来过
        cnt += 1
        if state == "right":
            if y != n - 1 and matrix[x][y + 1] != -999999:  # 可以向右走
                y += 1
                continue
            else:  # 要向下转了
                if x + 1 < m and matrix[x + 1][y] != -999999:  # 可以向下
                    x += 1
                    state = "down"
                    continue
        elif state == "down":
            if x != m - 1 and matrix[x + 1][y] != -999999:  # 可以向下走
                x += 1
                continue
            else:  # 要向左转
                if y > 0 and matrix[x][y - 1] != -999999:
                    y -= 1
                    state = "left"
                    continue
        elif state == "left":
            if y != 0 and matrix[x][y - 1] != -999999:
                y -= 1
                continue
            else:  # 要向上走
                if x != 0 and matrix[x - 1][y] != -999999:
                    x -= 1
                    state = "up"
                    continue
        elif state == "up":
            if x != 0 and matrix[x - 1][y] != -999999:
                x -= 1
                continue
            else:  # 右转
                if y != n - 1 and matrix[x][y + 1] != -999999:
                    y += 1
                    state = "right"
                    continue
    return res
ans = spiralOrder(data)
out_str = ''
for i in range(len(ans)):
    out_str += ','+ (str(ans[i]))
print(out_str[1:])