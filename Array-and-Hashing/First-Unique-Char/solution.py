from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        for ind, char in enumerate(s):
            if freq[char] == 1:
                return ind
        
        return -1