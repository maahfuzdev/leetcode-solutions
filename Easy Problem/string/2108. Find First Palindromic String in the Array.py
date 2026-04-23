class Solution(object):
    def firstPalindrome(self, words):
      result=[]
      for w in words:
        if w=="".join(list(w)[::-1]):
            return w
            result.append(w)
      if len(result)==0:
        return ""
      else:
        return result[0]            


        