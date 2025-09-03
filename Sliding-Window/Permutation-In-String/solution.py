from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        left, right = 0, 0
        first_freq = Counter(s1)
        curr, matches = 0, len(first_freq)
        s2_dict = {}

        while right < len(s1):
            char = s2[right]
            s2_dict[char] = s2_dict.get(char, 0) + 1

            if char in first_freq and first_freq[char] == s2_dict[char]:
                curr += 1
            
            right += 1
            
        while right < len(s2):
            if curr == matches:
                return True
            
            l_c = s2[left]
            r_c = s2[right]

            if l_c in first_freq and first_freq[l_c] == s2_dict[l_c]:
                curr -= 1
            
            s2_dict[l_c] -= 1
            left += 1

            s2_dict[r_c] = s2_dict.get(r_c, 0) + 1

            if r_c in first_freq and first_freq[r_c] == s2_dict[r_c]:
                curr += 1

            right += 1

        if curr == matches:
            return True
        return False