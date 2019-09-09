n = int(input())
res = 0
def f(m):
    count = 0
    while(m):
        count += m % 10
        m = m // 10
    return count

def g(m):
    count = 0
    while(m):
        count += m % 2
        m = m // 2
    return count

for i in range(n+1):
    if f(i) == g(i):
        res += 1
        #print(i)
    else:
        continue
print(res)
