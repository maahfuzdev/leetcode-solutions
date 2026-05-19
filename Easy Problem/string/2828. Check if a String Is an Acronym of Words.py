class Solution(object):
    def isAcronym(self, words, s):
        x=[]
        for w in words:
            x.append(w[0])
        return True if s=="".join(x) else False