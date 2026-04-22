class Solution(object):
    def reverseDegree(self, s):
        total = 0
        
        for i, ch in enumerate(s):
            rev_val = 26 - (ord(ch) - ord('a'))
            total += rev_val * (i + 1)
        
        return total