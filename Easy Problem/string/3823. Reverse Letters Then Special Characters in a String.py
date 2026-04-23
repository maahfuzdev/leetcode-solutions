class Solution(object):
    def reverseByType(self, s):
        
        al=[]
        sc=[]
        for i,v in enumerate(s):
            
            if v.isalpha():
                al.append(v)
            else:
                sc.append(v)     
        ral=al[::-1]
        rsc=sc[::-1]
        j=0
        k=0
        l=0
        result=[]
        while j<=len(ral) and k<=len(rsc) and l<len(s):
            if s[l].isalpha():
                result.append(ral[j])
                j+=1
                l+=1
            else:
                result.append(rsc[k])
                k+=1
                l+=1
        return "".join(result)            
