class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n = len(word)
        numSet = set()
        start = 0

        while start < n:
            if word[start].isdigit():
                curr = start
                while start < n and word[start].isdigit():
                    start += 1
                numSet.add(int(word[curr:start]))
            start += 1
        
        return len(numSet)
                
        