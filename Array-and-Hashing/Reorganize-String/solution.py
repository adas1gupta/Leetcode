from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        frequencies = Counter(s)

        heap = []
        for key, val in frequencies.items():
            heap.append([-val, key])
        
        heapq.heapify(heap)
        res = ""

        if max(frequencies.values()) > (len(s) + 1) // 2:
            return res
        
        while len(heap) >= 2:
            freq, char = heapq.heappop(heap)
            if len(res) == 0 or res[-1] != char:
                res += char
                freq += 1
            else:
                second, to_add = heapq.heappop(heap)
                res += to_add 
                second += 1
                if second < 0:
                    heapq.heappush(heap, [second, to_add])
            
            if freq < 0:
                heapq.heappush(heap, [freq, char])
        
        print(heap)
        _, char = heapq.heappop(heap)
        res += char
        return res
        