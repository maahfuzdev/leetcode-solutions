class Solution(object):
    def digitSum(self, s, k):

        while len(s) > k:

            l = []

            for i in range(0, len(s), k):
                l.append(s[i:i+k])

            s = []

            for j in range(len(l)):
                x = 0
                for p in range(len(l[j])):
                    x = x + int(l[j][p])
                s.append(str(x))
            s="".join(s)    

        return "".join(s)