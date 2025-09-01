class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_freq = 0
        freq = {}
        left, right = 0, 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]

            if (right - left + 1) - max_freq <= k:
                longest = max(longest, right - left + 1)
                
            else:
                while left <= right and (right - left + 1) - max_freq > k:
                    freq[s[left]] -= 1
                    left += 1

            right += 1
            
        return longest