class Solution(object):
    def twoSum(self, nums, target):
        dic = {}  # number → index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], i]
            dic[num] = i