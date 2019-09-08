n = int(input())
nums, data = [], []
res = []
for _ in range(n):
    nums = int(input())
    data = list(map(int, input().strip().split()))
    data.sort()
    count ={}
    for i in set(data):
        count[i] = data.count(i)
    b = max(count.values())
    if b <= len(data) / 2: print('YES')
    else: print('NO')

#
# T=int(input())
# for i in range(T):
#     n=int(input())
#     li=list(map(int,input().split()))
#     x = sorted(li)
#     m,n = 0,0
#     length = []
#     while m!=len(x) and n!=len(x):
#         if x[m]==x[n]:
#             n+=1
#         else:
#             length.append(n-m+1)
#             m+=1
#     if max(length)<=len(x)/2:
#         print('YES')
#     else:
#         print('NO')