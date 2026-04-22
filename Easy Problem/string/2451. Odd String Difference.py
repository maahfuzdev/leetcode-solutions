class Solution(object):
    def oddString(self, words):
        
        x=[]
        for i in range(len(words)):
            stack=[]
            for j in range(len(words[i])-1):
               stack.append(ord( words[i][j+1])-ord(words[i][j]))
            x.append(stack)
         # unique pattern খোঁজা
        for pattern in x:
            if x.count(pattern) == 1:
                return words[x.index(pattern)]

        