class Solution(object):
    def countPrefixes(self, words, s):
        l=[]
        c=0
        for i in range(len(s),0,-1):
            l.append(s[0:i])
        for j in words:
            if j in l:
                c+=1
        return c   