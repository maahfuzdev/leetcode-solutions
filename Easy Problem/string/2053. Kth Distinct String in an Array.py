class Solution(object):
    def kthDistinct(self, arr, k):
        freq = {}

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        distinct = []

        for x in arr:
            if freq[x] == 1:
                distinct.append(x)

        return distinct[k-1] if k <= len(distinct) else ""