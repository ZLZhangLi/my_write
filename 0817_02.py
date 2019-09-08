n,m = list(map(int,input().strip().split()))
w = list(map(int,input().strip().split()))
v = list(map(int,input().strip().split()))
s = min(w)
while(m):
    w = [i - s for i in w]
    a = w.index(0)
    b = v[w.index(0)]

    m -= sum(v[w.index(0)])
    s += 1
print(s)

# s = min(w)
# ww = [i-s for i in w]
# for i in range(len(ww)):
a = 1
