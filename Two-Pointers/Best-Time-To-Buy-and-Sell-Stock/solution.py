class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start, end = 0, 1

        while end < len(prices):
            max_profit = max(max_profit, prices[end] - prices[start]) 

            if prices[end] < prices[start]:
                start = end
            
            end += 1

        return max_profit