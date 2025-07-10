class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict = {}

        for char in magazine:
            noteDict[char] = noteDict.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in noteDict:
                return False
            elif noteDict[char] <= 0:
                return False
            else:
                noteDict[char] -= 1
        
        return True