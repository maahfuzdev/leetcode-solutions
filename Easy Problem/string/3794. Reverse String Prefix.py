class Solution(object):
    def reversePrefix(self, s, k):
       x=s[0:k]
       y=s[k:]
       return x[::-1]+y