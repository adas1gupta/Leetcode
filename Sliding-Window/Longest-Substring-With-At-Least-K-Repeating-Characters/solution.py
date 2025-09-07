class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        longest = 0

        for i in range(1, 27):
            s_dict = {}
            left, right = 0, 0
            curr = 0
            unique = 0

            while right < len(s):
                char = s[right]

                if char not in s_dict:
                    unique += 1

                s_dict[char] = s_dict.get(char, 0) + 1

                if s_dict[char] == k:
                    curr += 1
                
                while left <= right and unique > i:
                    if s_dict[s[left]] == k:
                        curr -= 1
                    
                    s_dict[s[left]] -= 1

                    if s_dict[s[left]] == 0:
                        del s_dict[s[left]]
                        unique -= 1
                    
                    left += 1
                
                if curr == unique and unique == i:
                    longest = max(longest, right - left + 1)
                
                right += 1
        
        return longest
