class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.word_arr = wordsDict
        self.word_ind = {}

        for ind, item in enumerate(wordsDict):
            if item not in self.word_ind:
                self.word_ind[item] = [ind]
            else:
                self.word_ind[item].append(ind)


    def shortest(self, word1: str, word2: str) -> int:
        fptr, sptr = 0, 0
        first = self.word_ind[word1]
        second = self.word_ind[word2]
        smallest = float('inf')

        while fptr < len(first) and sptr < len(second):
            smallest = min(smallest, abs(second[sptr] - first[fptr]))
            if first[fptr] < second[sptr]:
                fptr += 1
            else:
                sptr += 1
        
        return smallest


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)