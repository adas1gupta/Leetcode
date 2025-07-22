class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        for word in words:
            mappings = {}
            pair = {}
            matches = True
            for ind, char in enumerate(word):
                if char in mappings and pattern[ind] in pair:
                    if mappings[char] != pattern[ind] or pair[pattern[ind]] != mappings[char]:
                        matches = False
                        break
                elif char in mappings or pattern[ind] in pair:
                    matches = False
                    break
                else:
                    mappings[char] = pattern[ind]
                    pair[pattern[ind]] = mappings[char]
            
            if matches:
                ans.append(word)

        return ans
