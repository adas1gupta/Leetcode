class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        water = 0
        left, right = 0, len(height) - 1

        while left < right:       
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
                
            water += min(left_max, right_max) - min(height[left], height[right])

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return water