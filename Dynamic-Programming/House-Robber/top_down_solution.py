class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dp(i):
            if i >= n:
                return 0
            elif i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))

            return memo[i]
        
        return dp(0)