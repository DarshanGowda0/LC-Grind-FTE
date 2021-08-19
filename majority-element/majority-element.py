class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        same, count = nums[0], 0
        for n in nums:
            if count == 0:
                same = n
            if n == same:
                count += 1
            else:
                count -= 1
        
        return same