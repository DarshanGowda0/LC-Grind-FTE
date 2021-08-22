from heapq import * 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # 3 2 1 5 6 4
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        
        return heappop(heap)
            
        