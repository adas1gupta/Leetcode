class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        anagramResult = []

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - 97] += 1
            tupleCount = tuple(count)
            if tupleCount in anagramDict:
                anagramDict[tupleCount].append(string)
            else:
                anagramDict[tupleCount] = [string]
        
        for item in anagramDict:
            anagramResult.append(anagramDict[item])
        
        return anagramResult