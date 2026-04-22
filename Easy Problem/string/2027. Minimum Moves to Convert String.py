class Solution(object):
    
    def minimumMoves(self, s):
        moves = 0
        i = 0

        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3   # এক move এ ৩টা ঠিক
            else:
                i += 1   # কিছু করার দরকার নেই

        return moves