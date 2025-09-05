class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0] * len(nums1)
        my_map = {}

        for i,v in enumerate(nums2):
            my_map[v] = []
            for j in range(i+1,len(nums2)):
                if nums2[j] > v:
                    my_map[v].append(nums2[j])
        k = 0
        for i in nums1:
            if my_map[i]:
                result[k] = my_map[i][0]
            else:
                result[k] = -1
            k+=1
        return result
        

        


        