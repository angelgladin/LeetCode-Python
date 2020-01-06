# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + (r-l)//2
            x = guess(m)
            if x == -1:
                r = m-1
            elif x == 1:
                l = m+1
            else:
                return m
        return -1
