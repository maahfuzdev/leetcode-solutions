class Solution(object):
    def isIsomorphic(self, s, t):
        x=[]
        for i in range(len(s)):
            
            x.append(s[i]+t[i])
        return len(set(x)) == len(set(s)) == len(set(t))       

               




        