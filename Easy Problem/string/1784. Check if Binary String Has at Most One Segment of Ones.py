class Solution(object):
    def checkOnesSegment(self, s):
        x=[]
        y=''
        for i in range(len(s)):
            if s[i]=='1':
                y=y+s[i]
            else:
                if y!='':
                   x.append(y)
                   y=''
                else:
                    continue 
        if y!='':
             x.append(y)               
        return True if len(x)==1 else False              
        