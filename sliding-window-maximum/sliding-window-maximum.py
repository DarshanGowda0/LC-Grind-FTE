from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # naive is n*k
        # min heap is n * log k
        # deque n
        
        que = deque()
        res = []
        for idx, num in enumerate(nums):
            
            while que and nums[que[-1]] <= num:
                que.pop()
            
            que += idx, 
            
            if idx - que[0] >= k:
                que.popleft()
                
            if idx + 1 >= k:
                res += nums[que[0]],
        
        return res