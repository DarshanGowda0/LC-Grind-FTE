class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max, _min = float('-inf'), float('inf')
        res = 0
        for n in prices:
            if n < _min:
                _min = _max = n
            _max = max(n, _max)
            res = max(res, _max - _min)
            
        return res
            