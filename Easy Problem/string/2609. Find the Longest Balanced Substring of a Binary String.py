class Solution(object):
    def findTheLongestBalancedSubstring(self, s):

        r = []
        n = len(s)

        for i in range(n):
            for j in range(i+1, n+1):

                v = s[i:j]

                # check balanced
                if v == '0'*v.count('0') + '1'*v.count('1'):
                    if v.count('0') == v.count('1'):
                        r.append(len(v))

        return max(r) if r else 0