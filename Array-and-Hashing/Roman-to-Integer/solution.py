class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for ind, char in enumerate(s):
            if ind < len(s) - 1 and dictionary[s[ind + 1]] > dictionary[char]:
                total -= dictionary[char]
            else:
                total += dictionary[char]
        
        return total


