class Solution(object):
    def canBeEqual(self, s1, s2):
        # Even indices
        even1 = sorted(s1[0::2])
        even2 = sorted(s2[0::2])
        # Odd indices
        odd1 = sorted(s1[1::2])
        odd2 = sorted(s2[1::2])
        # Compare
        return even1 == even2 and odd1 == odd2