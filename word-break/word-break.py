class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mSet = set(wordDict)
        
        def recur(word, dp={}):
            if not word:
                return True
            
            if word in dp:
                return dp[word]
            
            for idx, c in enumerate(word):
                if word[:idx+1] in mSet:
                    ret = recur(word[idx+1:], dp)
                    dp[word[idx+1:]] = ret
                    if ret:
                        return ret
        
        return recur(s)
                
        