# 280. Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        for i in range(1, n-1, 2):
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
