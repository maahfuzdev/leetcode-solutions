class Solution(object):
    def numOfStrings(self, patterns, word):
        c=0
        for w in patterns:
            if w in word:
                c+=1
        return c