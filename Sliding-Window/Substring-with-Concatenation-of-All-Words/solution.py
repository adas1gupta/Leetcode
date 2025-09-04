from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_set = Counter(words)
        res = []
        window_size = len(words[0]) * len(words)

        if window_size > len(s):
            return res

        for offset in range(len(words[0])):
            left = offset
            anchor = offset
            right = window_size + offset
            window_set = {}
            curr, matches = 0, len(word_set)
    
            while left < right:
                word = s[left: left + len(words[0])]
                window_set[word] = window_set.get(word, 0) + 1

                if word in word_set and word_set[word] == window_set[word]:
                    curr += 1
                
                if curr == matches:
                    res.append(anchor)

                left += len(words[0])

            while right < len(s) - offset + 1:
                lw = s[anchor: anchor + len(words[0])]
                rw = s[right: right + len(words[0])]

                if lw in word_set and word_set[lw] == window_set[lw]:
                    curr -= 1
                
                window_set[lw] = window_set.get(lw, 0) - 1
                window_set[rw] = window_set.get(rw, 0) + 1

                if rw in word_set and word_set[rw] == window_set[rw]:
                    curr += 1
                
                if curr == matches:
                    res.append(anchor + len(words[0]))

                anchor += len(words[0])
                right += len(words[0])
        
        return res