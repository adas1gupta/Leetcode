class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest = len(wordsDict)
        first = -1
        second = -1

        for ind, word in enumerate(wordsDict):
            if word == word1 and second != -1:
                shortest = min(shortest, ind - second)
            elif word == word2 and first != -1:
                shortest = min(shortest, ind - first)
            
            if word == word1:
                first = ind
            elif word == word2:
                second = ind
        
        return shortest
