N, M = list(map(int, input().split()))
D = []
for _ in range(M):
    D.append(int(input()))

m = []
for i in range(N):
    temp = [i]
    for j in D:
        length = len(temp)
        for _ in range(length):
            ii = temp[0]
            temp.pop(0)
            if ii + j >= N and ii - j < 0:
                continue

            if ii + j < N:
                temp.append(ii + j)

            if ii - j >= 0:
                temp.append(ii - j)
        if not temp:
            break

    for j in temp:
        if j not in m:
            m.append(j)

print(len(m))

class Solution:
    def __init__(self, length):
        self.length = length
        self.end = set()

    def dfs(self, step, index, position):
        if position > self.length or position < 1:
            return
        if index == len(step):
            self.end.add(position)
            return
        self.dfs(step, index + 1, position + step[index])
        self.dfs(step, index + 1, position - step[index])


N, M = [int(n) for n in input().split()]
step = []
for _ in range(M):
    step.append(int(input()))
result = set()
for i in range(1, N + 1):
    s = Solution(N)
    s.dfs(step, 0, i)
    result = result | s.end
print(len(result))
