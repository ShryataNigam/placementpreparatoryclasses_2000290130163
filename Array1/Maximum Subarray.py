import functools
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=[]
        n=len(nums)
        if n==0 :
            return 0
        elif n==1:
            return max(nums)
        defaultSum=functools.reduce(lambda x,y:x+y,nums)
        a.append(defaultSum)
        dSum=0
        for i in nums:
            if dSum+i >= defaultSum:
                dSum=dSum+i
                a.append(i)
                a.append(dSum)
            elif dSum+i < defaultSum:
                 a.append(i)
                 dSum =0
        
        return max(a)  
