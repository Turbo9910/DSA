import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r = 0
        if len(nums) < k:
            return r
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k):
            r = -heapq.heappop(nums)
        return r

        