ll = list(map(int,input().strip().split()))
up = 0
down = 0
m_res = True
def f(m,res):
    for i in range(len(m) - 1):
        if m[i] < m[i + 1]:
            up = 1
            for j in range(i+1,len(m)-1):
                if m[j] > m[j + 1]:
                    down = 1
                    for k in range(j+1,len(m)-1):
                        if m[k] < m[k+1]:
                            res = False

        elif m[i] > m[i + 1]:
            down = 1
            for j in range(i+1,len(m)-1):
                if m[j] < m[j + 1]:
                    up = 1
                    for k in range(j+1,len(m)-1):
                        if m[k] > m[k+1]:
                            res = False
    return res
print(f(ll,m_res))