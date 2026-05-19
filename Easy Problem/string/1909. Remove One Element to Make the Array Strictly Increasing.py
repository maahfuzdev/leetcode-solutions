class Solution(object):
    def canBeIncreasing(self, nums):
        removed = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                removed += 1
                if removed > 1:
                    return False

                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]

        return True