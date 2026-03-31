class Solution(object):
    def isPalindrome(self, x):
       clist =list(str(x))
       newlist=[]
       for i in range(len(clist)-1,-1,-1):
        newlist.append(clist[i])
       if clist==newlist:
        return True
       return False 

        