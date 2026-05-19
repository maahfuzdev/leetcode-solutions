from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        pos = defaultdict(list)

        # store indices of each value
        for i, v in enumerate(nums):
            pos[v].append(i)

        res = [0] * len(nums)

        # process each value group
        for arr in pos.values():
            n = len(arr)

            # prefix sums
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + arr[i]

            # calculate distance
            for i in range(n):
                idx = arr[i]

                left = i * arr[i] - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - (n - i - 1) * arr[i]

                res[idx] = left + right

        return res