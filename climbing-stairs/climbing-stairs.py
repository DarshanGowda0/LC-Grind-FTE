class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
            