class Solution(object):
    def findValidPair(self, s):
        from collections import Counter
        
        count = Counter(s)

        for i in range(len(s)-1):
            a = s[i]
            b = s[i+1]

            if (
                a != b and
                count[a] == int(a) and
                count[b] == int(b)
            ):
                return a + b

        return ""