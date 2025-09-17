class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = list()
        c_map = {}
        for i in nums1:
            if i in c_map:
                c_map[i] +=1
            else:
                c_map[i] = 1

        for i in nums2:
            if i in c_map and c_map[i] != 0:
                    r.append(i)
                    c_map[i] -=1
        return r


        