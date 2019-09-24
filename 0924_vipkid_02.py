data = list(map(int,input().strip().split()))
k = int(input())
res = []
for i in range(len(data) - k + 1):
    total = 0
    for j in range(i,i+k):
        total += data[j]
    avg = round(total / k,3)
    res.append(avg)
# print(res)
# print ([' '.join(str(i)) for i in res])
for i in res:
    print('%.2f'%(i),end = ' ')