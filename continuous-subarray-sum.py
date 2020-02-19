# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i]
        for i in range(n-1):
            for j in range(i+1, n):
                sum_ = dp[j] - dp[i] + nums[i]
                if sum_ == k or (k != 0 and sum_ % k == 0):
                    return True
        return False
