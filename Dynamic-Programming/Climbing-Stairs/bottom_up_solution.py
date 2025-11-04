class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 2)]
        dp[n + 1] = 0
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]

#Build out the tree and cross out redundant portions until you can compress the tree into a line. 

#This line is [curr = prev_one + prev_two, prev_one = prev_two + prev_three, ..., arr[n - 1] = arr[n] + arr[n + 1]]

#This line means creating an array that computes position i from position i + 1 and i + 2. 
#So n - 1 will need n, which is 1, and n + 1, which is 0 (an overshoot)

