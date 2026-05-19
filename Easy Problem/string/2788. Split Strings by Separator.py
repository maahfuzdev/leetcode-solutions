class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        result=[]
        for w in words:
            j=0
            for i in range(len(w)):
                
                if w[i]==separator :
                    if w[j:i]!="":
                       result.append(w[j:i])
                    j=i+1
            if w[j:len(w)]!="":
                result.append(w[j:len(w)])    
        return result            
        