# n = int(input())
n = 10
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ",end="")      # 打印n-i个空格
        j += 1
    k = 1
    while k <= 2*i-1:
        if k == 1 or k == 2*i-1 or i == n or i == n-1:      # 当k等于1或2i-1（第一个或最后一个）或i等于n（最后一行）时打印星号
            print("*",end="")
        else:
            print(" ",end="")      # 否则打印空格
        k += 1
    print("")
    i += 1

# for i in range(n):
#     for j in range(n-2-1):
#         print(" ", end="")
#     print('*')
#     for j in range(2*(n-2-1)):
#         print(" ", end="")
#     print('*')
#     for j in range(n-2-1):
#         print(" ", end="")