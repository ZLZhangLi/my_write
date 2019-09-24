N,M = list(map(int,input().strip().split()))
data1 = sorted(list(map(int,input().strip().split())))
data2 = sorted(list(map(int,input().strip().split())))
pro = []
for i in data1:
    for j in data2:
        pro += [abs(i*j)]
pro.sort()
print(pro[-2])