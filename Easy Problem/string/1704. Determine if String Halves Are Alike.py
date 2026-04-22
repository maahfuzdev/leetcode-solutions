class Solution(object):
    def halvesAreAlike(self, s):
        vowel=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l=len(s)
        first=s[:l//2]
        second=s[l//2:]
        x=0
        y=0
        for i in range(len(first)):
            if first[i] in vowel:
                x+=1
            if second[i] in vowel:
                y+=1
        if x==y:
            return True
        else:
            return False                
        