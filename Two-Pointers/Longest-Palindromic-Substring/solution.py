class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        for ind, char in enumerate(s):
            start, end = ind, ind

            while start >= 0 and end < len(s) and s[start] == s[end]:
                end += 1
                start -= 1
            
            if end - start > len(longest):
                longest = s[start + 1: end]

            start, end = ind, ind + 1

            while start >= 0 and end < len(s) and s[start] == s[end]:
                end += 1
                start -= 1
            
            if end - start > len(longest):
                longest = s[start + 1: end]
        
        return longest