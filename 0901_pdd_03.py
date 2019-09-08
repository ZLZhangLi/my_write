from tkinter import _flatten
n,m,k = list(map(int,input().strip().split()))
mm = []
for i in range(n):
    mm.append([])
    for j in range(m):
        mm[i].append(0)

for i in range(n):
    for j in range(m):
        mm[i][j] = (i + 1) * (j + 1)
mm = list(_flatten(mm))
mm.sort(reverse = True)
print(mm[k - 1])
# res = []
# for i in range(n):
#     for j in range(m):
#         res.append(mm[i][j])
# res = sorted(res,reverse = True)
# print(res[k-1])
