n = int(input())
m = list(map(int,input().strip().split()))
for i in range(2,n):
    sum = 0
    a = []
    for j in range(i+1):
        a.append(m[j])
    for k in a:
        sum+=k

    if sum > 2*max(a):
        print (i + 1)
        break
    if i == n - 1:
        sum < 2 * max(a)
        print(-1)