class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0 for _ in range(length)]
        
        for start, end, incr in updates:
            res[start] += incr
            if end < length - 1:
                res[end+1] -= incr
            
        for i in range(1, length):
            res[i] += res[i-1]
            
        return res