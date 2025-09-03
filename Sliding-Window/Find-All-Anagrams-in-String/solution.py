from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        anag = Counter(p)
        left, right = 0, 0
        curr, matches = 0, len(anag)
        start_list = []
        s_dict = {}

        while right < len(p):
            char = s[right]
            s_dict[char] = s_dict.get(char, 0) + 1

            if char in anag and s_dict[char] == anag[char]:
                curr += 1
            
            if curr == matches:
                start_list.append(left)

            right += 1
        
        while right < len(s):
            lc = s[left]
            rc = s[right]

            if lc in anag and anag[lc] == s_dict[lc]:
                curr -= 1

            s_dict[lc] -= 1
            s_dict[rc] = s_dict.get(rc, 0) + 1
            
            if rc in anag and anag[rc] == s_dict[rc]:
                curr += 1
            
            if curr == matches:
                start_list.append(left + 1)

            left += 1
            right += 1
        
        return start_list