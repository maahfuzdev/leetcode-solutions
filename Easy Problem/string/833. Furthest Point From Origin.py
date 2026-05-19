class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        
        l=moves.count('L')
        r=moves.count('R')
        s=moves.count('_')
        if l>r:
            return abs(l+s-r) 
        else:
            return abs(r+s-l)               
        