class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = left + (right - left) // 2
            mid = nums[m]

            if mid == target:
                return m
            
            elif nums[left] <= mid:
                if nums[left] <= target < mid:
                    right = m - 1
                else:
                    left = m + 1
            
            else:
                if mid < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1
                    
        return -1
