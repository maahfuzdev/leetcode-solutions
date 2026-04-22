class Solution(object):
    def freqAlphabets(self, s):
        result = []
        i = 0

        while i < len(s):
            # case 10# to 26#
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                result.append(chr(num + 96))
                i += 3
            else:
                result.append(chr(int(s[i]) + 96))
                i += 1

        return "".join(result)