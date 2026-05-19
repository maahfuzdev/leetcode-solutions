class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        total = 0

        for w in words:
            if set(w) <= allowed_set:
                total += 1

        return total