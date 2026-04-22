class Solution(object):
    def percentageLetter(self, s, letter):
        ch=0
        for i in s:
            if i==letter:
                ch+=1
        return (ch*100)//len(s)