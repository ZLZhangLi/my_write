#荷兰国旗问题 颜色分类
def sortColors(nums):
    curr = 0
    p = 0
    q = len(nums) - 1
    for i in range(len(nums)):
        if nums[curr] == 0:
            tmp = nums[p]
            nums[p] = nums[curr]
            nums[curr] = tmp
            p += 1
            curr += 1
        elif nums[curr] == 2:
            tmp = nums[q]
            nums[q] = nums[curr]
            nums[curr] = tmp
            q -= 1
        else:
            curr += 1
    return nums

nums = list(map(int,input().strip().split(',')))
res = sortColors(nums)
for i in res:
    print(i,end=',')