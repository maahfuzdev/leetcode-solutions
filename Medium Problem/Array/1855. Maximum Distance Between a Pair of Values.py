class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0
        j = 0
        n, m = len(nums1), len(nums2)
        ans = 0

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i

        return ans