class Solution(object):
    def restoreString(self, s, indices):
      dic1={}
      list1=[]
      x=sorted(indices)
      for i in range(len(s)):
        dic1[indices[i]]=s[i]
      for i in range(len(s)):  
        list1.append(dic1[x[i]])
      return ''.join(list1)