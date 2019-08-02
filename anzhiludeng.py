N = int(input())
i = 0
pos_nums = []
pos = []
while i < N:
    a = int(input())
    b = list(input().strip().split())
    if len(b) == 1:
        pos_nums.append(a)
        pos.append(b)
    i += 1

for i in range(len(pos)):
    c = pos[i][0]
    for j in range(len(pos[i][0])):
        print (pos[i][0][j])