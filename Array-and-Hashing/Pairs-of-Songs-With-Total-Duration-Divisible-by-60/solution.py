class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = {}
        total = 0

        for ind, item in enumerate(time):
            pair = item % 60
            if pair in pairs and pair == 0:
                total += pairs[pair]
            elif 60 - pair in pairs:
                total += pairs[60 - pair]
            pairs[pair] = pairs.get(pair, 0) + 1
            
        return total
                