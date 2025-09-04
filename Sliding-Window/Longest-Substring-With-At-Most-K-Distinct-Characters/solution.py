class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        s_dict = {}
        longest = 0
        left, right = 0, 0

        while right < len(s):
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1

            while len(s_dict) > k and left <= right:
                char = s[left]
                s_dict[char] -= 1

                if s_dict[char] <= 0:
                    del s_dict[char]
                
                left += 1
            
            longest = max(longest, right - left + 1)
            
            right += 1

        return longest