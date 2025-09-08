class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        current_sum = sum(cardPoints[len(cardPoints) - k:])
        max_sum = current_sum 
        
        for i in range(k):
            current_sum += cardPoints[i]
            current_sum -= cardPoints[len(cardPoints) - (k - i)]
            max_sum = max(max_sum, current_sum)
        
        return max_sum