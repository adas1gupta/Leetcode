class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = Counter(nums)

        for key, val in freq.items():
            buckets[val].append(key)
        
        res = []
        for item in buckets[::-1]:
            for num in item:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        
        return res