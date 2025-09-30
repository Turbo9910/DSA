class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        
        for i in num_set:
            if i - 1 not in num_set:  
                c = 1
                while i + c in num_set:
                    c += 1
                count = max(count, c)
        
        return count

        
        