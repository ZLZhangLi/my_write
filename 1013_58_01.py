data = list(map(int,input().strip().split()))
n = data[0]
m = data[1]
num = data[2:]
def second_index(li):
    a = sorted(set(li))
    return li.index(a[1])
for i in range(m):
    m_min = min(num)
    m_second_min_index = second_index(num)
    m_second_min = num[m_second_min_index]
    num.append(m_second_min + m_min)
    num.remove(m_min)
    num.remove(m_second_min)
print(min(num))