class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        s1=[]
        for i in s:
            s1.append(i[::-1])
        return " ".join(s1)    

       
        