class Solution(object):
    def compareBitonicSums(self, nums):
        jorvanelik = nums 
        dic={}
        for i,v in enumerate(nums):
            dic[v]=i
        x=max(nums)
        p_in=dic[x]
        acen_ar=nums[0:p_in+1]
        dec_ar=nums[p_in:]
        sum_as=sum(acen_ar)
        sum_de=sum(dec_ar)
        if sum_as==sum_de:
            return -1
        elif sum_as>sum_de:
            return 0
        else:
            return 1
        