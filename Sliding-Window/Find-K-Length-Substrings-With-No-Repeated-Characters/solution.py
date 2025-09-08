class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        s_dict = {}
        total = 0
        left, right = 0, 0

        while right < len(s):
            while s[right] in s_dict or right - left + 1 > k:
                s_dict[s[left]] -= 1

                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]
                
                left += 1
            
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1

            if right - left + 1 == k:
                total += 1
            
            right += 1
        
        return total