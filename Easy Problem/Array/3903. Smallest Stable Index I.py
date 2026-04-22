class Solution(object):
    def firstStableIndex(self, nums, k):
        x=[]
        l=len(nums)
        for i in range(l):
            if max(nums[0:i+1])-min(nums[i:l])<=k:
                x.append(i)

        if len(x)==0:
            return -1
        else:
            return min(x)            
          
        class Solution(object):
    def firstStableIndex(self, nums, k):
        x=[]
        l=len(nums)
        for i in range(l):
            if max(nums[0:i+1])-min(nums[i:l])<=k:
                x.append(i)

        if len(x)==0:
            return -1
        else:
            return min(x)            
          
        