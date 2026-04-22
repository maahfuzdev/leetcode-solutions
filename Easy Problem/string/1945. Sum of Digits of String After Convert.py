class Solution(object):
    def getLucky(self, s, k):

        # Step 1: convert letters to numbers
        num = ""
        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        # Step 2: repeat digit sum k times
        for _ in range(k):
            total = 0
            for d in num:
                total += int(d)
            num = str(total)

        return int(num)