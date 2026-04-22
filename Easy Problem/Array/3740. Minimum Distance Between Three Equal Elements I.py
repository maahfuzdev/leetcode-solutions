class Solution(object):
    def minimumDistance(self, nums):

        from collections import defaultdict

        pos = defaultdict(list)

        # store indices
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = float('inf')

        # check each number
        for v in pos:
            arr = pos[v]

            if len(arr) >= 3:
                for i in range(len(arr) - 2):
                    i1 = arr[i]
                    i3 = arr[i+2]

                    dist = 2 * (i3 - i1)
                    ans = min(ans, dist)

        return ans if ans != float('inf') else -1

        