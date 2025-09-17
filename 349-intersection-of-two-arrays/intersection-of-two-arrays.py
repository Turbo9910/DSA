class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = list()
        if len(nums1) == 0 or len(nums2) == 0:
            return r
        c_map = Counter(nums1)

        for i in nums2:
            if i in c_map and  i not in r:
                r.append(i)
        return r


              