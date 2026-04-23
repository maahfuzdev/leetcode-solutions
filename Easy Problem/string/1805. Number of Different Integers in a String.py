class Solution(object):
    def numDifferentIntegers(self, word):
        word=list(word)
        x=[]
        y=[]
        z=[]
        for i,v in enumerate(word):
            if v.isdigit() :
                y.append(v)
            else:
                if len(y)!=0:
                    x.append("".join(y))
                    y=[]
                else:
                    continue
        x.append("".join(y))        
                    
        for j in x:
            if j!="":
                z.append(int(j))
        return len(set(z))                        

        
        