class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        end = 1
        max_profit = 0

        while end < len(prices):
            if prices[end] > prices[end - 1]:
                max_profit += prices[end] - prices[end - 1]

            end += 1
        
        return max_profit