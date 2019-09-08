# n = int(input())
# x = list(map(int,input().strip().split()))
# p = []
# for i in range(len(x)):
#     p.append([])
#     for j in range(x[i]):
#         p[i].append(1.0 / x[i])
# print(p)

def func(x,nums):
    t = 1
    NN = 1
    p = 0
    for i in nums:
        if i >= x:
            NN *= i
            p += 1
    while(p):
        if p&1:
            t *= x
        x = x*x
        p >>= 1
    return t / NN
n = int(input())
data = [int(i) for i in input().split()]
data.sort()
Nmax = max(data)
res = 0
for i in range(1,Nmax+1):
    ff = func(i,data)
    ff = ff - func(i - 1,data)
    res += ff * i
print('%0.2f'%res)