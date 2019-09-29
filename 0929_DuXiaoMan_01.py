N,W = list(map(int,input().strip().split()))
w = list(map(int, input().strip().split()))
t = list(map(int, input().strip().split()))
time = []
count = 0
m_time = 0

while w:
    time = []
    count = 0
    for i in range(len(w)):
        count += w[i]
        time.append(t[i])
        if count <= W:
            if i == len(w) - 1:
                m_time += max(time)
                w = []
                break
            else:
                continue
        else:
            count -= w[i]
            time.pop()
            m_time += max(time)
            w = w[i:]
            t = t[i:]
            break
print(m_time)