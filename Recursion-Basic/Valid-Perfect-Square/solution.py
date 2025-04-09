class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def helper(left, right):
            if left > right:
                return right

            mid = left + ((right - left) // 2)

            if mid * mid == num:
                return mid
            elif mid * mid <= num:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)
        
        result = helper(0, num)
        return ((result * result) == num)