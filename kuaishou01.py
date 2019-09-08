n = int(input())
m = int(input())
data = []
for i in range(m):
    data.append(input())
b = data[0][0]
for i in range(len(data)):
    if data[i][0] == 'P':
        #print(i)
        if i < m - n + 1:
            for j in range(i+1,i+n):
                num = 0
                if data[j][0] == 'P':
                    for k in range(j,m):
                        if num != n-1:
                            if data[k][0] == 'V':
                                tmp = data[k]
                                del data[k]
                                data.insert(j+num,tmp)
                                num += 1
                            # elif k == m -1 and data[k][0] == 'P':
                            #     del data[k]
                        else:
                            break
        else:
            break
a = []
for i in range(len(data)-n+1,len(data)):
    num = 0
    for j in range(i - n + 1,i+1):
        if data[j][0] == 'P':
            num += 1
        else:
            continue
    if num > 1:
        a.append(i)
a.sort(reverse=True)
for i in a:
    del data[i]
print(len(data))
for i in data:
    print(i)