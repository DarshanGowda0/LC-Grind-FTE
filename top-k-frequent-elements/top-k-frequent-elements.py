from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for num, freq in c.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
                
        return [i for _, i in heap]