class Solution(object):
    def isSubstringPresent(self, s):
        x=s[::-1]
        c=0
        for i in range(len(s)-1):
            if s[i:i+2] in x:
                c+=1
        return True if c>0 else False    


        
        