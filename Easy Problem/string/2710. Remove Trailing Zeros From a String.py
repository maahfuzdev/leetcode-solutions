class Solution(object):
    def removeTrailingZeros(self, num):
        num=list(num)
        for i in range(len(num)-1,0,-1):
            if num[i]=='0':
                num.pop()
            else:
                break
        return "".join(num)            
        