class Solution(object):
    def diStringMatch(self, s):
        low = 0
        high = len(s)
        result = []

        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        result.append(low)   # last number
        return result