class Solution(object):
    def maximumValue(self, strs):
        l=[]
        for v in strs:
            if v.isdigit():
                l.append(int(v))
            else:
                l.append(len(v))
        return max(l)            
        