class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):

        i = 0
        n = min(len(s1), len(s2), len(s3))

        while i < n and s1[i] == s2[i] == s3[i]:
            i += 1

        # যদি একদম কোন common prefix না থাকে
        if i == 0:
            return -1

        # মোট অপারেশন = বাকি অংশ কেটে ফেলা
        return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)