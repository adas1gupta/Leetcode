from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        charCount = Counter(word)
        freqCount = Counter(charCount.values())

        if len(freqCount) == 1:
            freq = list(freqCount.keys())

            return freq[0] == 1 or len(charCount) == 1
        elif len(freqCount) == 2:
            freqs = sorted(list(freqCount.keys()))
            first, second = freqs[0], freqs[1]

            if freqCount[first] == 1 and first == 1:
                return True
            elif second - 1 == first and freqCount[second] == 1:
                return True
            return False 
        else:
            return False