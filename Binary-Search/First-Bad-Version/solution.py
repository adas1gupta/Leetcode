# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            m = left + (right - left) // 2

            if isBadVersion(m) == True:
                right = m - 1
            elif isBadVersion(m) == False:
                left = m + 1
        
        return right + 1