class Solution(object):
    def balancedStringSplit(self, s):
        count=0
        r=0
        for i in range(len(s)):
            if s[i]=="R":
                r+=1
            else:
                r-=1
            if r==0:
                count+=1
        return count                

        
        