class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_count = {}
        for i,v in enumerate(nums):
            needed = target - v
            if needed in nums_count:
                return [nums_count[needed],i]
                
            nums_count[v] = i
        
        

        