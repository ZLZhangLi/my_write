import os
result = []
Ai = []
xh = []
i, DP = 0, []
N, M = list(map(int, input().split()))

for index in range(N):
    v = list(map(int, input().split()))
    if len(v) == 2:
        DP.append(v)

while len(Ai) != M:
    Ai = list(map(int, input().split()))
# from collections import defaultdict
#
# DP = defaultdict(int, DP)
#
# ma = 0
# d = sorted(list(DP.keys()) + Ai)
# for i in d:
#     ma = max(DP[i], ma)
#     DP[i] = ma
# for i in Ai:
#     print(DP[i])
for m in range(len(Ai)):
    xh = []
    salary = 0
    temp = 0
    for j in DP:
        if Ai[m] > j[0] or Ai[m] == j[0]:
            temp = j[1]
            if salary < temp:
                salary = temp
            #xh.append(j[1])
        else:
            continue
            #xh.append(0)
    #result.append(max(xh))
    result.append(salary)
for n in result:
    print (n)

# N, M = list(map(int, input().split()))
# i, DP = 0, []
# while i < N:
#    v = list(map(int, input().split()))
#    if len(v) == 2:
#        DP.append(v)
#        i += 1
# Ai = []
# while len(Ai) != M:
#     Ai = list(map(int, input().split()))
# from collections import defaultdict
#
# DP = defaultdict(int, DP)
#
# ma = 0
# d = sorted(list(DP.keys()) + Ai)
# for i in d:
#     ma = max(DP[i], ma)
#     DP[i] = ma
# for i in Ai:
#     print(DP[i])