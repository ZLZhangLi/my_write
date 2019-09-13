m = int(input())
k = int(input())
m_list = [0] * m
def jiechen(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
def func(m,k,a):
    a[m-1] = k
    for i in range(m-2,-1,-1):
        a[i] = a[i+1] + jiechen(i+1) + 1
func(m,k,m_list)
ans = sum(m_list)
print(ans)
