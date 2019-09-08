import copy
def perm(lis,begin,end):
    if begin>=end:
        a = copy.deepcopy(lis)
        output.append(a)
    else:
        i = begin
        for num in range(begin,end):
            lis[num],lis[i] = lis[i],lis[num]
            perm(lis,begin+1,end)
            lis[num],lis[i] = lis[i],lis[num]
N = int(input())
M = list(map(int, input().strip().split()))

lis = list(range(1,N+1))
output = []
perm(lis,0,len(lis))
a = sorted(output)
for index in range(len(a)):
    if M == a[index]:
        result = a[-index-1]
for index in result:
   print(index, end=' ')