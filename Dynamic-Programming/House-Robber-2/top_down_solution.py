class Solution:
    def rob(self, nums: List[int]) -> int:
        first = {}
        second = {}
        n = len(nums)

        if n == 1:
            return nums[0]

        def dp(i, last, memo):
            if i in memo:
                return memo[i]
            if i >= last:
                return 0
            
            memo[i] = max(nums[i] + dp(i + 2, last, memo), dp(i + 1, last, memo))
        
            return memo[i]
        
        return max(dp(0, n - 1, first), dp(1, n, second))