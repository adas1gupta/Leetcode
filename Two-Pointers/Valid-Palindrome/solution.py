class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        
        while start < end:
            left = s[start]
            right = s[end]
            if not left.isalnum():
                start += 1
                continue
            if not right.isalnum():
                end -= 1
                continue

            if left.lower() != right.lower():
                return False
            start += 1
            end -= 1
        
        return True