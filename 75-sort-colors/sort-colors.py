class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_map = Counter(nums)

        for i in range(len(nums)):
            if c_map[0] != 0:
                nums[i] = 0
                c_map[0] -=1
            elif c_map[1] != 0:
                nums[i] = 1
                c_map[1] -=1
            else:
                nums[i] = 2
                c_map[2] -=1
        

        

        