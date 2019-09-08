n = int(input())
i = 0
second = []
third = []
total = 0
while i < n:
    second.append(int(input()))
    third.append(list(map(int, input().strip().split())))
    i += 1

# for j in range(len(second)):
#     l1 = sorted(third[j])
#     for k in range(len(l1)):
#         if l1[k] < l1[(k+1) % len(l1)] + l1[(k-1) % len(l1)]:
#             total += 1
#         else:
#             total += 0
#     if total == len(l1):
#         print ('YES')
#     else:
#         print('NO')
for j in range(len(second)):
    l1 = sorted(third[j])
    if l1[-1] < l1[-2] + l1[0]:
        print ('YES')
    else:
        print('NO')