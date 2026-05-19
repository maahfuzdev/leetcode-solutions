class Solution(object):
    def generateTheString(self, n):
        res=[]
        if n%2==0:
            for i in range(n-1):
                res.append("a")
            res.append("b")    
            return "".join(res) 
        else:  
            for i in range(n):
                res.append("a") 
            return "".join(res)        


        