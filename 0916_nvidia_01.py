m = int(input())
n = []
for _ in range(m):
    n.append(list(map(int,input().strip().split())))
data = []
for _ in range(4):
    data.append(list(map(int,input().strip().split())))
def func(gird):
    if gird == 0:
        gird = 1
    else: gird = 0
    return  gird
def filp1(A0,f):
    def filp1_2(A,ff):
        x = ff[0] - 1
        y = ff[1] - 1
        if x > 0 and y > 0 and x < 3 and y < 3:
            A[x][y - 1] = func(A[x][y - 1])
            A[x][y + 1] = func(A[x][y + 1])
            A[x - 1][y] = func(A[x - 1][y])
            A[x + 1][y] = func(A[x + 1][y])
        elif x > 0 and x < 3 and y == 3:
            A[x][y - 1] = func(A[x][y - 1])
            A[x - 1][y] = func(A[x - 1][y])
            A[x + 1][y] = func(A[x + 1][y])
        elif y > 0 and x == 3 and y < 3:
            A[x][y - 1] = func(A[x][y - 1])
            A[x][y + 1] = func(A[x][y + 1])
            A[x - 1][y] = func(A[x - 1][y])
        elif x == 0 and y > 0 and y < 3:
            A[x][y - 1] = func(A[x][y - 1])
            A[x][y + 1] = func(A[x][y + 1])
            A[x + 1][y] = func(A[x + 1][y])
        elif y == 0 and x > 0 and x < 3:
            A[x][y + 1] = func(A[x][y + 1])
            A[x - 1][y] = func(A[x - 1][y])
            A[x + 1][y] = func(A[x + 1][y])
        elif y == 0 and x == 0:
            A[x][y + 1] = func(A[x][y + 1])
            A[x + 1][y] = func(A[x + 1][y])
        elif y == 3 and x == 3:
            A[x][y - 1] = func(A[x][y - 1])
            A[x - 1][y] = func(A[x - 1][y])
        return A
    for i in f:
        ans = filp1_2(A0, i)
    return ans
def filp2(A0,f):
    def filp2_2(A,ff):
        x = ff[0] - 1
        y = ff[1] - 1
        if x > 0:
            A[x - 1][y] = func(A[x - 1][y])
        if x < 3:
            A[x + 1][y] = func(A[x + 1][y])
        if y > 0:
            A[x][y - 1] = func(A[x][y - 1])
        if y < 3:
            A[x][y + 1] = func(A[x][y + 1])
        return A
    for i in f:
        ans = filp2_2(A0,i)
    return ans
#res = filp1(data,n)
res = filp2(data,n)
for i in range(4):
    for j in range(4):
        print(res[i][j],end=' ')
    print('\n')