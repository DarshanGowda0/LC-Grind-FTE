class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer technique 
        # move the lower height ptr, when both are same either should work, cuz the area is limited by the lowest height anyways
        
        left, right = 0, len(height) - 1
        res = float('-inf')
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return res