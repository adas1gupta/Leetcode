class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            width = r - l
            leftH = heights[l]
            rightH = heights[r]
            maxArea = max(maxArea, width * min(leftH, rightH))

            if leftH <= rightH:
                l += 1
            else:
                r -= 1
        
        return maxArea