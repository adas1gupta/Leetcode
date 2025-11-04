class Solution:
    def climbStairs(self, n: int) -> int:
        end, overshoot = 1, 0

        for i in range(n - 1, -1, -1):
            end, overshoot = end + overshoot, end
        
        return end