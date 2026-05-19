class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels="aeiou"
        c=0
        for i in range(left,right+1,1):
            n=len(words[i])-1
            if words[i][0] in vowels and words[i][n] in vowels:
                c+=1
        return c        
        
        