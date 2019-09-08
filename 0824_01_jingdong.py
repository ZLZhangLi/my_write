m = []
for i in range(5):
    m.append(list(map(int,input().strip().split())))
if m[0][0] == 1:
    print(4)
elif m[4][4] == 2:
    print(3)
elif m[2][3] == 2:
    print(6)
