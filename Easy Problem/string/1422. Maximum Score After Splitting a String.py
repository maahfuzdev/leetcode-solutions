class Solution(object):
    def maxScore(self, s):
        left=[]
        right=[]
        x=[]
        i=1
        while i<len(s):
            left.append(s[:i])
            right.append(s[i:])
            x.append("".join(left).count("0")+"".join(right).count("1"))
            left=[]
            right=[]
            i+=1
        return max(x)    
        