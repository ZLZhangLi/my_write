n = int(input())
m = []
for _ in range(n):
    m.append(int(input()))
#
# m_sort1 = sorted(m)
# m_sort2 = m_sort1[::-1]
# res1 = 0
# res2 = 0
# for i in range(n):
#     res1 += abs(m_sort1[i] - m[i])
# for i in range(n):
#     res2 += abs(m_sort2[i] - m[i])
#
# res = min(res1,res2)
# print(m_sort1)
# print(m_sort2)
# print(res)

class Solution:
    def minSwap(self, A,B):
        n = len(A)
        huan = 1
        buhuan = 0
        for i in range(1,n):
            if A[i]>A[i-1]:#本来就不用换
                if A[i]>B[i-1] and B[i]>A[i-1]:#换了也满足
                    huan = min(huan,buhuan)+1#那么i次换就是i-1次的小值加1次
                    buhuan = huan-1
                else:#换了前面的也要跟着换
                    huan += 1
            else:#本来需要换
                t = buhuan
                buhuan = huan#如果i不换那么交换前面的
                huan = t+1
        return min(huan,buhuan)

a = Solution()
print(a.minSwap(m,m))