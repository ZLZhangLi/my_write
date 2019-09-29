data = list(map(int,input().strip().split(',')))
class Solution:
    def func(self,nums):
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < len(nums) - 1:
            end = max(end,nums[start] + start)
            start += 1
        return end >= n - 1
a = Solution()
if a.func(data):
    print(1)
else:
    print(0)