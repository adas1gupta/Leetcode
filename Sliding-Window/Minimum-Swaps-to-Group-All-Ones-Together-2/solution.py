from collections import Counter
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        freq = Counter(data)
        left, right = 0, freq.get(1, 0)
        curr = Counter(data[:right])
        window = curr.get(1, 0)
        max_freq = curr.get(1, 0)

        while right < len(data) + freq.get(1, 0):
            ind = right % len(data) 
            if data[ind] == 1:
                window += 1
            if data[left] == 1:
                window -= 1

            max_freq = max(max_freq, window)
            left += 1
            right += 1
        
        return freq.get(1, 0) - max_freq