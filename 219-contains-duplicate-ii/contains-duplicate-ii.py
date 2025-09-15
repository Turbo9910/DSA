class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] in mapping:
                j = mapping[nums[i]]
                if abs(i - j) <= k:
                    return True
            mapping[nums[i]] = i
        return False

        