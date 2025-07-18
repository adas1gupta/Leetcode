class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similarSet = set()

        for key, val in similarPairs:
            similarSet.add((key, val))

        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            first = sentence1[i]
            second = sentence2[i]

            if (first, second) not in similarSet and (second, first) not in similarSet and first != second:
                return False
        
        return True