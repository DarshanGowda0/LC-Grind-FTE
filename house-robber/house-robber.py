class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp - calculate the profit if I rob the current huz or skip robbing the curremt huz
        # if I rob the current huz, then don;t rob the next huz
        
        def recur(nums, idx, dp={}):
            if idx >= len(nums):
                return 0
            
            if idx not in dp:
                robCurrent = nums[idx] + recur(nums, idx+2, dp)
                skipCurrent = recur(nums, idx+1, dp)
            
                dp[idx] = max(robCurrent, skipCurrent)
                
            return dp[idx]
        
        return recur(nums, 0)