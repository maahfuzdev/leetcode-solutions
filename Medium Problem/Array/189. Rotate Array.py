class Solution(object):
    def rotate(self, nums, k):
        dic = {}
        n = len(nums)

        for i in range(n):
            dic[(i+k) % n] = nums[i]

        values_list = [v for k,v in sorted(dic.items())]

        nums[:] = values_list   # ⭐ MAIN FIX