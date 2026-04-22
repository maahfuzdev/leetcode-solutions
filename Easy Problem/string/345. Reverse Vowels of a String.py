class Solution(object):
    def reverseVowels(self, s):
        v=['a','e','i','o','u','A','E','I','O','U']
        list1=list(s)
        ind=[]
        vow=[]
        for i,k in enumerate(list1):
            if k in v:
                ind.append(i)
                vow.append(k)
        vow=vow[::-1]
        for j in range(len(ind)):
            list1[ind[j]]=vow[j]
        return "".join(list1)            
        