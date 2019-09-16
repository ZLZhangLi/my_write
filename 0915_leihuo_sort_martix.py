n = int(input())
m = list(map(int,input().strip().split()))
s = []
wh = []
w = []
for i in range(0,len(m),2):
    s.append(m[i] * m[i+1])
    wh.append(min(m[i]/m[i+1],m[i+1]/m[i]))
    w.append(m[i])

for _ in range(3):
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if s[j] > s[j + 1]:
                m[2 * j], m[2 * j + 2] = m[2 * j + 2], m[2 * j]
                m[2 * j + 1], m[2 * j + 3] = m[2 * j + 3], m[2 * j + 1]
                s[j], s[j + 1] = s[j + 1], s[j]
                wh[j], wh[j + 1] = wh[j + 1], wh[j]
                w[j], w[j + 1] = w[j + 1], w[j]
            elif s[j] == s[j+1]:
                if wh[j] < wh[j+1]:
                    m[2 * j], m[2 * j + 2] = m[2 * j + 2], m[2 * j]
                    m[2 * j + 1], m[2 * j + 3] = m[2 * j + 3], m[2 * j + 1]
                    wh[j], wh[j + 1] = wh[j + 1], wh[j]
                    w[j], w[j + 1] = w[j + 1], w[j]
                elif wh[j] == wh[j+1]:
                    if w[j] > w[j+1]:
                        m[2 * j], m[2 * j + 2] = m[2 * j + 2], m[2 * j]
                        m[2 * j + 1], m[2 * j + 3] = m[2 * j + 3], m[2 * j + 1]
                        w[j], w[j + 1] = w[j + 1], w[j]
                    else:
                        continue
                else:
                    continue
            else:
                continue

for i in range(len(m)):
    print(m[i],end = ' ')
