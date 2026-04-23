class Solution(object):
    def largestGoodInteger(self, num):
        y = []
        i = 0

        while i < len(num) - 2:
            if num[i] == num[i+1] == num[i+2]:
                y.append(num[i:i+3])
                i += 3   # skip this block
            else:
                i += 1

        return max(y) if y else ""