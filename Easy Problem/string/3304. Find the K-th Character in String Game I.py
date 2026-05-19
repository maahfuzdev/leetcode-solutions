class Solution(object):
    def kthCharacter(self, k):

        word = "a"

        while len(word) < k:
            nxt = ""

            for c in word:
                nxt += chr((ord(c)-97+1)%26 + 97)

            word += nxt

        return word[k-1]