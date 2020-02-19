# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        def aux(s, dp, i, n):
            if i == n:
                return 1
            elif i > n:
                return 0
            if dp[i] == -1:
                c = 0
                if s[i] != 0:
                    c += aux(s, dp, i+1, n)
                if i+1 < n and (s[i] == 1 or (s[i] == 2 and s[i+1] < 7)):
                    c += aux(s, dp, i+2, n)
                dp[i] = c
            return dp[i]
        n = len(s)
        dp = [-1]*n
        nums = [int(x) for x in s]
        return aux(nums, dp, 0, n)
