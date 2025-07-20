import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)

        most_freq = 0
        reigning = {}
        to_return = None
        words = paragraph.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower().split()

        for item in words:
            reigning[item] = reigning.get(item, 0) + 1
        
        for key, val in reigning.items():
            if val > most_freq and key not in banned:
                most_freq = val
                to_return = key

        return to_return