#n,k = list(map(int,input().strip().split()))
# m = list(map(int,input().strip().split()))
m = [3,1,2,3,1,4]
K = 2
num = 0
for k in range(K):
    for i in range(len(m)-1):
        if m[i] % 3 !=0:
            for j in range(i + 1,len(m)):
                flag = 0
                if m[j]%3 != 0:
                    a = m[i] + m[j]
                    if a%3 == 0:
                        m.remove(m[j])
                        m.remove(m[i])
                        m.append(a)
                        flag = 1
                        break
                else:
                    continue
            if flag == 1:
                break
        else:
            continue

for i in range(len(m)):
    if m[i] % 3 == 0:
        num+=1
print(num)