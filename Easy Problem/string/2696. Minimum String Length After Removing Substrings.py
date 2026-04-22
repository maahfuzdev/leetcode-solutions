class Solution(object):
    def minLength(self, s):
        s = list(s)
        i = 0

        while i < len(s) - 1:
            if "".join(s[i:i+2]) in ("AB", "CD"):
                del s[i:i+2]
                i = 0
            else:
                i += 1

        return len(s)