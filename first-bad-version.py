# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_search(n):
            l, r = 1, n
            while l < r:
                m = l + (r-l)//2
                if isBadVersion(m):
                    r = m
                else:
                    l = m +1
            return r
        return binary_search(n)