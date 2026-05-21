class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        r=[]
        for i in range(len(A)):
            common=list(set(A[:i+1]) & set(B[:i+1]))
            r.append(len(common))
        return r    
        