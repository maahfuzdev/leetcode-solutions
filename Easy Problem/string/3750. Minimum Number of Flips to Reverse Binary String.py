class Solution(object):
    def minimumFlips(self, n):
        b=""
        while n>0:
            b=str(n%2)+b
            n=n//2
        b=list(b)
        r=b[::-1]
        c=0
        for i in range(len(b)):
            if b[i]!=r[i]:
                c+=1
        return c        


        
        