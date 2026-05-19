class Solution(object):
    def countElements(self, nums):

        mn = min(nums)
        mx = max(nums)

        count = 0

        for x in nums:
            if mn < x < mx:
                count += 1

        return count