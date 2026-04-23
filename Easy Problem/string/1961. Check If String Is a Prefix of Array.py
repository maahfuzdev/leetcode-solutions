class Solution(object):
    def isPrefixString(self, s, words):
        c=0
        for i in range(1,len(words)+1,1):
            if s=="".join(words[0:i]):
                 c+=1
                
        if c==1:
            return True
        else:
           return False           


        