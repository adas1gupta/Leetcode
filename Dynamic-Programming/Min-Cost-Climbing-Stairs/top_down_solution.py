class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        #recurrence relation is memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))
        def dp(i):
            if i >= len(cost):
                return 0
            elif i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))

            return memo[i]

        return min(dp(0), dp(1))
