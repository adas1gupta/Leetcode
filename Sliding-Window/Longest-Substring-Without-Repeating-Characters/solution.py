class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anchor, scanner = 0, 0
        maximum = 0
        freq = {}

        while scanner < len(s):
            char = s[scanner]

            if char not in freq or freq[char] <= 0:
                maximum = max(maximum, scanner - anchor + 1)
            else:
                while freq[char] > 0:
                    freq[s[anchor]] -= 1
                    anchor += 1
                    
            freq[char] = freq.get(char, 0) + 1
            scanner += 1

        return maximum