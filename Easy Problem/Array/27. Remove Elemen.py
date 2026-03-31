class Solution(object):
    def removeElement(self, nums, val):
        i = 0  # next position for non-val element
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # original nums পরিবর্তন
                i += 1
        return i  # k = number of non-val elements