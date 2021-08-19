class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 pointers, one points to zero boundary, other moves as iterator
        zeroPtr, idx = 0, 0
        for idx, num in enumerate(nums):
            if not num:
                zeroPtr = idx
                break
        else:
            return

        while idx < len(nums):
            if nums[idx] != 0:
                nums[idx], nums[zeroPtr] = nums[zeroPtr], nums[idx]
                zeroPtr += 1
            idx += 1
            
                
                
            