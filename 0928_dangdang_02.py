s1,s2,s3 = input().split()
class Solution:
    def func(self,s1,s2,s3):
        from collections import deque
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        queue = deque()
        queue.appendleft((0,0))
        visited = set()
        while queue:
            i, j = queue.pop()
            if i == n1 and j == n2:
                return True
            if i < n1 and s1[i] == s3[i + j] and (i + 1,j) not in visited:
                visited.add((i + 1,j))
                queue.appendleft((i + 1,j))
            if j <  n2 and s2[j] == s3[i + j] and (i,j+1) not in visited:
                visited.add((i,j + 1))
                queue.appendleft((i,j + 1))
        return False
a = Solution()
if a.func(s1,s2,s3):
    print(1)
else:
    print(0)