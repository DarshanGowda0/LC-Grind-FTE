class Solution:
    def longestPalindrome(self, s: str) -> str:
        # you check if s[i] and s[i+k] is same and s[i+1][i+k-1] is already a palindrome
        if not s:
            return ""
        
        k = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest, res = 0, ""
        
        n = len(s)
        
        for i in range(n):
            dp[i][i] = True
        
        longest = 1
        res = s[-1]
            
        k = 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest = 2
                res = s[i:i+2]
        
        # 2 - 3
        for k in range(2, n):
            for i in range(n - k):
                if s[i] == s[i+k] and dp[i+1][i+k-1]:
                    dp[i][i+k] = True
                    longest = k+1
                    res = s[i:i+k+1]
                    
        return res
                    
        