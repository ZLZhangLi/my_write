import math
n,m = list(map(int,input().strip().split()))
data = []
for _ in range(n):
    data.append(input())
def comb_1(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
print(comb_1(m-1,2) * 8)