class Solution(object):
    def maxDistance(self, colors):
        x=[]
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors),1):
                if colors[i]!=colors[j]:
                    x.append(abs(i-j))
        return max(x)            
        
        