n = int(input())
i = 0
xy = []
x = []
y = []
while(i < n):
    xy.append(list(map(int,input().strip().split())))
    i += 1
for i in xy:
    x.append(i[0])
for i in xy:
    y.append(i[1])
w = max(x) - min(x)
h = max(y) - min(y)
if w < h:
    a = h
else:
    a = w
print (a ** 2)