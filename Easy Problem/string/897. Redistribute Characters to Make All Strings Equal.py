class Solution(object):
    def makeEqual(self, words):
        from collections import Counter
        count=Counter()
        for v in words:
            count=count+Counter(v)
        n=len(words)
        for i in count.values():
            if i%n!=0:
                return False
        return True        



           

        