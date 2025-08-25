class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        local_count = 0

        for i in nums:
            if i:
                local_count+=1
                if local_count > max_count:
                    max_count = local_count
            else:
                local_count=0
        return max_count
      
        