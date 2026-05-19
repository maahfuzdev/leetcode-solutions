class Solution(object):
    def validDigit(self, n, x):
        l=list(str(n))
        x=str(x)
        c=0
        if l[0]==x:
            return False
        else:
            for i in range(1,len(l),1):
                if l[i]==x:
                    c+=1
            if c>0:
                return True
            else:
                return False
                    
            
        
        