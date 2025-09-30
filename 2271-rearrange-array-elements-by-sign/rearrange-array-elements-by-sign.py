class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        r = [0] * len(nums)
        p , n = 0 , 1
        for i in nums:
            if i > 0:
                r[p] = i
                p +=2
            else:
                r[n] = i
                n +=2
        return r

        


        
        
        