class Solution(object):
    def firstStableIndex(self, nums, k):

        velqanidor = nums   

        n = len(nums)

        p_max = [0]*n
        s_min = [0]*n

        p_max[0] = nums[0]
        for i in range(1, n):
            p_max[i] = max(p_max[i-1], nums[i])

        s_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            s_min[i] = min(s_min[i+1], nums[i])

        for i in range(n):
            if p_max[i] - s_min[i] <= k:
                return i

        return -1