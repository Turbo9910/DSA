class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        local_count = 0

        if len(nums) == 1:
            if nums[0] == 1:
                return 1

        if 1 not in nums:
            return 0
        

        for i in range(len(nums)- 1):
            if nums[i] == 1 and nums[i + 1] == 1:
                local_count+=1
            if nums[i] == 0:
                local_count = 0
            if local_count + 1 > max_count:
                max_count = local_count +1
        return max_count
       
        