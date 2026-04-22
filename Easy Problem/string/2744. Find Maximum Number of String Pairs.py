class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        n= len(words)
        c=0
        for i in range(n-1):
            for j in range(i+1,n,1):
                if words[i]=="".join(list(words[j])[::-1]):
                    c+=1
        return c            
        
        