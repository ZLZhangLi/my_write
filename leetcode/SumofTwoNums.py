#字典求两数之和 双指针的方法。
nums = [1,7,2,7,15]
target = 9
hashmap = {}
for index, num in enumerate(nums):
    another_num = target - num
    if another_num in hashmap:
        print([hashmap[another_num], index])
    hashmap[num] = index
#a = 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m_dict = {}
        for i in range(len(nums)):
            m_dict[nums[i]] = i
        for i in range(len(nums)):
            if target- nums[i] in m_dict.keys():
                return [i,m_dict[target- nums[i]]]