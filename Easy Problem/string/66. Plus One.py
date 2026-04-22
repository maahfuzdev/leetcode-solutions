class Solution(object):
    def plusOne(self, digits):
        y = []

        for v in digits:
            y.append(str(v))   # int → string

        x = int("".join(y)) + 1

        return [int(d) for d in str(x)]