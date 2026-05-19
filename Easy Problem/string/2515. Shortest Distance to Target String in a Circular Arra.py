class Solution(object):
    def closestTarget(self, words, target, startIndex):
        res=[]
        n=len(words)
        for i in range(n):
            if target==words[i]:
                res.append(min(abs(startIndex-i),abs(n-1-i+startIndex+1),abs(n-startIndex+i)))
        if len(res)>0:
            return min(res)
        else:
            return -1    
        