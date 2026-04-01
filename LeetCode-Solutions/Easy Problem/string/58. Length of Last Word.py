class Solution(object):
    def lengthOfLastWord(self, s):
        j=0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                break
            else:
                j+=1
        return j        
        