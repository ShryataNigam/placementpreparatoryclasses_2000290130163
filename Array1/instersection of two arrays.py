class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
           
        n=len(nums1)
        m=len(nums2)
        k=n+m
        a=[]
        for i in range(0,n):
            for j in range(0,m):
                if (nums2[j]==nums1[i]):
            
                    a.append(nums2[j])
                    nums1[i]=-1
                    nums2[j]=-1
                    break
         
        
        return a;
