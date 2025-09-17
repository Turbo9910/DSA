class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = list()
        if len(nums) == 0:
            return r
        c_map = Counter(nums)

        for i in range(1,len(nums)+1):
            if i not in c_map:
                r.append(i)
        return r
        