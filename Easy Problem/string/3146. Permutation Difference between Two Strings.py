class Solution(object):
    def findPermutationDifference(self, s, t):
        dic1={}
        for i,v in enumerate(t):
            dic1[v]=i
        sum=0
        for j,val in enumerate(s):
            sum=sum+abs(j-dic1[val]) 
        return sum       
        