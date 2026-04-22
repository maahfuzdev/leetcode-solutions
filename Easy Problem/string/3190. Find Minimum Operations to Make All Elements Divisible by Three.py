class Solution(object):
    def minimumOperations(self, nums):
        x=0
        for i in nums:
            if i%3!=0:
                x=x + min(abs(i%3 -3),abs(i%3 -0))

        return x