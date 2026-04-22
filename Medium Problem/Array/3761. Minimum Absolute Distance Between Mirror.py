class Solution(object):
    def minMirrorPairDistance(self, nums):

        seen = {}
        ans = float('inf')

        for i, num in enumerate(nums):

            rev = int(str(num)[::-1])

            # check mirror pair
            if num in seen:
                ans = min(ans, i - seen[num])

            # ALWAYS update latest index
            seen[rev] = i

        return -1 if ans == float('inf') else ans