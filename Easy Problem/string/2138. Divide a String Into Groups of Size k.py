class Solution(object):
    def divideString(self, s, k, fill):
        tem=[]
        i=0
        res=[]
        while i<len(s):
            tem=s[i:i+k]
            i+=k
            if len(tem)!=k:
                tem=list(tem)
                for _ in range(k-len(tem)):
                    tem.append(fill)
                res.append("".join(tem))  
            else:
                res.append(tem)
        return res              
        