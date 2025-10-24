class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = left + (right - left) // 2
            num = nums[m]

            if num > target:
                right = m - 1
            elif num == target:
                return m
            else:
                left = m + 1
        
        return right + 1