class Solution(object):
    def mirrorDistance(self, n):
        x=str(n)[::-1]
        return abs(int(x)-n)
        