# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, l, r = [1]*n, [1]*n, [1]*n
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        for i in range(n):
            ans[i] = l[i] * r[i]
        return ans
