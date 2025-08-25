class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)

        for key,value in nums_count.items():
            if value == 1:
                return key

        