from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_freq = Counter(t)
        s_dict = {}
        left, right = 0, 0
        min_string = float('inf')
        start, end = 0, 0
        curr, matches = 0, len(t_freq)
        
        while right < len(s):
            char = s[right]
            s_dict[char] = s_dict.get(char, 0) + 1

            if char in t_freq and t_freq[char] == s_dict[char]:
                curr += 1
            
            while curr == matches:
                window_size = right - left + 1
                
                if min_string > window_size:
                    min_string = window_size
                    start, end = left, right
                
                char = s[left]
                s_dict[char] -= 1

                if char in t_freq and s_dict[char] < t_freq[char]:
                    curr -= 1
                
                left += 1
            
            right += 1
        
        return s[start:end + 1] if min_string != float('inf') else ""