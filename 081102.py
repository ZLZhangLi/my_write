l,n = list(map(int, input().strip().split()))
m = list(map(int, input().strip().split()))
d = []
avg = 0
r = 0
for i in range(len(m)):
    avg += m[i] / n

for i in range(len(m)):
    a = m[i] - avg
    r += a
print (r - n)