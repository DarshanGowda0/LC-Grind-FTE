class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force - n^2
        # kadane's - calculate sum of prev elements, make prevSum 0 if prevSum is < 0
        
        prevSum = nums[:]
        for i in range(1, len(prevSum)):
            prevSum[i] = max(prevSum[i], prevSum[i-1] + prevSum[i])
            
        return max(prevSum)
            