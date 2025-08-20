class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 1
        unique = 0
        while end < len(nums):
            if nums[end] != nums[end - 1]:
                start += 1
                unique += 1
                nums[start] = nums[end]
                
            end += 1
        
        return unique + 1