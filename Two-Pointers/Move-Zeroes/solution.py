class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor, scanner = 0, 0

        while scanner < len(nums):
            if nums[scanner] != 0:
                nums[anchor], nums[scanner] = nums[scanner], nums[anchor]
                anchor += 1
            
            scanner += 1