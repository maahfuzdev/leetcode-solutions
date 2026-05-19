class Solution(object):
    def hasSameDigits(self, s):
        def mod(s):
            x=''
            for i in range(len(s)-1):
                x=x+str((int(s[i])+int(s[i+1]))%10)
            return x
        y=mod(s)
        while len(y)>2:
            y=mod(y)        
        return y[0] == y[1]