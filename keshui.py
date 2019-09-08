n , k = list(map(int,input().strip().split()))
ai = []
ti = []
value0 = 0
value1 = 0
value2 = []
value3 = []
value4 = []
result = 0
while len(ai) != n and len(ti) != n:
    ai = list(map(int,input().strip().split()))
    ti = list(map(int,input().strip().split()))
# for i in range(n):
#     value0 = 0
#     if ti[i] == 1:
#         value1 += ai[i]
#     elif ti[i] == 0:
#         if i < n - 2:
#             value0 += ai[i] + ai[i + 1] + ai[i + 2]
#             if ti[i + 1] == 1:
#                 value0 -= ai[i + 1]
#             if ti[i + 2] == 1:
#                 value0 -= ai[i + 2]
#         elif i == n - 2:
#             value0 += ai[i] + ai[i + 1]
#             if ti[i + 1] == 1:
#                 value0 -= ai[i + 1]
#         elif i == n - 1:
#             value0 += ai[i]
#         value2.append(value0)
#
# value3 = value1 + max(value2)
# print (value3)

for i in range(n):
    if ti[i] == 1:
        value1 += ai[i]
    else:
        value2.append(ai[i])
        value3.append(i)


for index in range(len(value3)):
    value0 = 0
    for j in range(len(value2)):
        if j + index < len(value2):
            if value3[j + index] < value3[index] + k:
                value0 += value2[j + index]
        else:
            value0 += 0
    value4.append(value0)

#value3 = value1 + max(value4)
print (value1 + max(value4))
