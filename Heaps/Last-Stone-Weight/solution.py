class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-s for s in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
            first = heapq.heappop(negative_stones)
            second = heapq.heappop(negative_stones)

            first = -first
            second = -second
            print(first, second)
            if first > second:
                heapq.heappush(negative_stones, -(first - second))
        
        return 0 if len(negative_stones) == 0 else -(negative_stones[0])