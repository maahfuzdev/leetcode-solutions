class Solution(object):
    def maximumStrongPairXor(self, nums):
        l=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i] -nums[j])<=min(nums[i],nums[j])and nums[i]!=nums[j]:
                    l.append(nums[i]^nums[j])
        return max(l) if len(l)!=0 else 0           




        
        