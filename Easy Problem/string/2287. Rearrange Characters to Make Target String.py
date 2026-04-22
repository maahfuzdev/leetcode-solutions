class Solution(object):
    def rearrangeCharacters(self, s, target):

        from collections import Counter

        s_count = Counter(s)
        t_count = Counter(target)

        result = float('inf')

        for char in t_count:
            result = min(result, s_count[char] // t_count[char])

        return result