class Solution(object):
    def countSegments(self, s):
        segment = 0

        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i-1] == " "):
                segment += 1

        return segment