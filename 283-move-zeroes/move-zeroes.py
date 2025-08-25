class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = list()
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(nums[i])
                zeros.append(0)
            else:
                i+=1
        for i in range(len(zeros)):
            nums.append(zeros[i])
        

            
        