class Solution(object):
    def minOperations(self, s):
        diff1 = diff2 = 0

        for i, c in enumerate(s):
            if c != str(i % 2):
                diff1 += 1
            if c != str((i + 1) % 2):
                diff2 += 1

        return min(diff1, diff2)