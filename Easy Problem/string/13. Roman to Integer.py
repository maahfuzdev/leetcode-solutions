class Solution(object):
   def romanToInt(self, s):
     rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     sum=rom[s[len(s)-1]]
     if len(s)==1:
        return sum
     else:    
        for i in range(len(s)-2,-1,-1):
         
           if rom[s[i]]>=rom[s[i+1]]:
              sum=sum+rom[s[i]]
           else:
              sum=sum-rom[s[i]]
        return sum       

        