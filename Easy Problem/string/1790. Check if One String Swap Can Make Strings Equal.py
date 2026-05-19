class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1==s2:
            return True
        c=0 
        x=sorted(s1)
        y=sorted(s2)
        if x==y: 
              for i in range(len(s1)):
                   if s1[i]!=s2[i]:
                      c+=1
              if c==2:
                 return True
              else:
                 return False 
        else :
            return False            
                    
        
        