# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = { x : i for (i, x) in enumerate(nums)}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in s and s[x] != i:
                return [i, s[x]]
        return []
