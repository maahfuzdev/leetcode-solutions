class Solution(object):
    def similarPairs(self, words):
        c=0
        for i in range(len(words)-1):
            v="".join(sorted(list(set(words[i]))))
            for j in range(i+1,len(words),1):
                w="".join(sorted(list(set(words[j]))))
                if v==w:
                    c+=1
        return c            
        