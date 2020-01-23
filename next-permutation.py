# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l, i, j):
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
        
        def reverse(l, i, j):
            while i < j:
                swap(l, i, j)
                i += 1
                j -= 1
        
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            k = n-1
            while k >= 0 and nums[k] <= nums[i]:
                k -= 1
            swap(nums, i, k)
        
        reverse(nums, i+1, n-1)
