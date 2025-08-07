from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        numFreq = Counter(nums)
        to_return = []

        for item in set(nums):
            freq = numFreq[item]
            buckets[freq - 1].append(item)
        
        for i in range(len(buckets) - 1, -1, -1):            
            arr = buckets[i]

            for item in arr:
                if len(to_return) == k:
                    return to_return
                to_return.append(item)
        
        return to_return