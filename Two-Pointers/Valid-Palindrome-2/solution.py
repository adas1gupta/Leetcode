class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            left, right = s[start], s[end]

            if left != right:
                l_a = s[start + 1: end + 1]
                r_a = s[start:end]
                return l_a == l_a[::-1] or r_a == r_a[::-1]
            else:
                start += 1
                end -= 1
        
        return True        