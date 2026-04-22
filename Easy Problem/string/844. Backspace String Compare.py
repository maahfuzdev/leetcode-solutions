class Solution(object):
    def backspaceCompare(self, s, t):
       x=[]
       y=[]
       for i in range(len(s)):
          if s[i]=="#" and len(x)>0:
            x.pop()
          elif s[i]!="#":
            x.append(s[i])
             
       for j in range(len(t)):
          if t[j]=="#" and len(y)>0:
            y.pop()
          elif t[j]!="#":
            y.append(t[j])     

             
       if x==y:
          return True
       else:       
          return False   