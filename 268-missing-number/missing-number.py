class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_counter = Counter(nums)

        for i in range(len(nums) + 1):
            if i not in num_counter:
                return i
        