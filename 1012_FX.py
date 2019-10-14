n = int(input())
res = 0
def func(num):
    ans = int(num)
    for i in num:
        ans += int(i)
    return ans

for i in range(n):
    fx = func(str(i))
    flag = 0
    for j in range(i+1,n):
        fy = func(str(j))
        if fx == fy:
            flag = 1
            break
    if flag == 0:
        res += 1
print(res)