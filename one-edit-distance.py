# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1:
            return False
        if ns > nt:
            return self.isOneEditDistance(t, s)

        if ns == nt:
            diff = 0
            for i in range(ns):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1
        else:
            i, j = 0, 0
            diff = 0
            while i < ns and j < nt:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    diff += 1
            return diff == 1 or i == j
