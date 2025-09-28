import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        i = heapq.heappop(nums) + 1
        j = heapq.heappop(nums) + 1

        return i * j
        
        