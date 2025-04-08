class Solution:
    def mySqrt(self, x: int) -> int:
        def helper(left, right):
            if left > right:
                return right

            mid = left + ((right - left) // 2)

            if mid * mid == x:
                return mid
            elif mid * mid <= x:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)
        
        return helper(0, x)
