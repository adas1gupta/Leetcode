class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        smallest = float('inf')
        total = 0

        while left <= right < len(nums):
            total += nums[right]

            while total >= target:
                smallest = min(smallest, right - left + 1)
                total -= nums[left]
                left += 1
           
            right += 1  
        
        return smallest if smallest != float('inf') else 0