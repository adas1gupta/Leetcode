class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(start, i, memo):
            if i < start: return 0
            if i in memo: return memo[i]

            memo[i] = max(nums[i] + dp(start, i - 2, memo), dp(start, i - 1, memo))
            return memo[i]
        
        return max(dp(1, len(nums) - 1, {}), dp(0, len(nums) - 2, {}))