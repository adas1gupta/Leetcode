class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        
        word_dict = {}
        result = set()

        for ind, word in enumerate(words):
            word_dict[word] = ind
        
        for i, word in enumerate(words):
            n = len(word)
            
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if suffix[::-1] in word_dict and is_palindrome(prefix) and word_dict[suffix[::-1]] != i:
                    result.add((word_dict[suffix[::-1]], i))
                
                if prefix[::-1] in word_dict and is_palindrome(suffix) and word_dict[prefix[::-1]] != i:
                    result.add((i, word_dict[prefix[::-1]]))

        return [list(pair) for pair in result]