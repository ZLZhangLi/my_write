import collections
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        # 1. Color each component.
        # colors[node] = the color of this node.

        N = len(graph)
        colors = {}
        c = 0

        def dfs(node, color):
            colors[node] = color
            for nei, adj in enumerate(graph[node]):
                if adj and nei not in colors:
                    dfs(nei, color)

        for node in range(N):
            if node not in colors:
                dfs(node, c)
                c += 1

        # 2. Size of each color.
        # size[color] = number of occurrences of this color.
        size = collections.Counter(colors.values())

        # 3. Find unique colors.
        color_count = collections.Counter()
        for node in initial:
            color_count[colors[node]] += 1

        # 4. Answer
        ans = float('inf')
        for x in initial:
            c = colors[x]
            if color_count[c] == 1:
                if ans == float('inf'):
                    ans = x
                elif size[c] > size[colors[ans]]:
                    ans = x
                elif size[c] == size[colors[ans]] and x < ans:
                    ans = x

        return ans if ans < float('inf') else min(initial)

n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int,input().strip().split())))
init = list(map(int,input().strip().split()))

a = Solution()
print(a.minMalwareSpread(m,init))