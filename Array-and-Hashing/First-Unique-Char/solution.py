from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        longest = 0
        hasUneven = False

        for k, v in charCount.items():
            if v % 2 == 1:
                hasUneven = True
            
            longest += (v // 2) * 2
        
        return longest + 1 if hasUneven else longest