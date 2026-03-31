class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""  # result string
        i, j = 0, 0  # index for word1 and word2

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        # যদি word1 বাকি থাকে
        if i < len(word1):
            merged += word1[i:]

        # যদি word2 বাকি থাকে
        if j < len(word2):
            merged += word2[j:]

        return merged
        