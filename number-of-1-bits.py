# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = (1<<32)-1
        flag = 1
        ans = 0
        for i in range(32):
            if flag & n:
                ans += 1
            flag <<= 1
        return ans
