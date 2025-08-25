class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = Counter(nums)
        limit = len(nums) //2
        for key,value in nums_map.items():
            if value > limit:
                return key
        