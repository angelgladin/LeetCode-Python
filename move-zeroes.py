# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while i < n:
            if nums[i] != 0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
                j += 1
            i += 1
