n,m = list(map(int,input().strip().split()))
# 先初始化全是0的矩阵
arr = []
for _ in range(n):
    arr.append(list(map(int,input().strip().split())))
# n = int(raw_input('>'))
#初始化数组
# arr = [[0]*n for i in range(n)]
#递归解决
def dfs(arr, x, y, start, n):
    if n<=0:return 0
    if n==1:
        arr[x][y] = start
        return 0
    #up
    for i in range(n):
        arr[x][y+i] = start
        start += 1
    #right
    for i in range(n-1):
        arr[x+1+i][y+n-1] = start
        start += 1
    #down
    for i in range(n-1):
        arr[x+n-1][y+n-2-i] = start
        start += 1
    #left
    for i in range(n-2):
        arr[x+n-2-i][y] = start
        start += 1
    dfs(arr,x+1,y+1,start,n-2)

a = dfs(arr,0,0,1,n)
#格式化输出print
l = len(str(n*n))+1
format = ('%'+str(l)+'d')*n
for tmp in arr:
    print (format%tuple(tmp))