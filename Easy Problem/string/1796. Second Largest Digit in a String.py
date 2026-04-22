class Solution(object):
    def secondHighest(self, s):
        x=set()
        for i in s:
            if i.isdigit():
                x.add(int(i))
        y=sorted(list(x),reverse=True)
        if len(y)>=2:
            return y[1]
        else:
            return -1   

                

        