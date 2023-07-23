
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


        """
        x=len(nums1)
        y=len(nums2)
        nums1=nums1[0:x-y]
        nums1=map(str,nums1)
        nums1="".join(nums1)
        nums2=map(str,nums2)
        nums2="".join(nums2)
        nums3=nums1+nums2
        #nums3.strip()
        nums1=[]
        for i in nums3:
            nums1.append(int(i))
            nums1=sorted(nums1)
        

        print(nums1)
        #map(int,nums1)
        


        Do not return anything, modify nums1 in-place instead.
        """
