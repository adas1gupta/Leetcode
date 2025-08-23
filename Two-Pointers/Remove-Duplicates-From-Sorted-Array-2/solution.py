class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hold, scan = 0, 0
        count = 1

        while hold <= scan < len(nums):
            if 0 < scan and nums[scan] == nums[scan - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[hold] = nums[scan]
                hold += 1

            scan += 1
        
        return hold