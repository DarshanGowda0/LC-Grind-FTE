class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = nums[:]
        for idx, val in enumerate(nums):
            if temp[val - 1] > 0:
                temp[val - 1] *= -1
            # print(temp)
        
        result = []
        for idx, n in enumerate(temp):
            if n > 0:
                result += idx + 1,
                
        return result
                