class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        from collections import Counter
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # all characters from both words
        all_chars = set(word1 + word2)
        
        for ch in all_chars:
            if abs(count1[ch] - count2[ch]) > 3:
                return False
        
        return True