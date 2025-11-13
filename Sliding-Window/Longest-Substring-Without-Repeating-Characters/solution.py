class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        freq = {}

        while right < len(s):
            char = s[right]

            freq[char] = freq.get(char, 0)

            while freq[char] > 0:
                freq[s[left]] -= 1
                left += 1
            
            freq[char] += 1
            right += 1

            longest = max(longest, right - left)
            
        return longest
