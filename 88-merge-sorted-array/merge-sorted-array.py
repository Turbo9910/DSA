from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = list()
        if m == 0:
            for i in range(m+n):
                nums1[i] = nums2[i]
            return

    
        for i in range(m):
            nums.append(nums1[i])

        p = len(nums)
        i = 0
        j = 0
        k = 0
        while i < p and j < n:
            if nums[i] <= nums2[j]:
                nums1[k] = nums[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1

        if j < n:
            while j < n:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        else:
            while i < p:
                nums1[k] = nums[i]
                k += 1
                i += 1

        return nums1  
