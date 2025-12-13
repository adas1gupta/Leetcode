class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        anchor, scanner = 1, 1

        while scanner < len(nums):
            if nums[scanner] != nums[scanner - 1]:
                nums[anchor] = nums[scanner]
                anchor += 1
            
            scanner += 1
        
        return anchor
