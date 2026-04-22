class Solution(object):
    def getMinDistance(self, nums, target, start):
        list1=[]
        for i,v in enumerate(nums):
            if v==target:
                  list1.append(abs(start-i))
        return int(min(list1))         

        