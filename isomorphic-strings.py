# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = dict()
        m2 = dict()
        for i in range(len(s)):
            if (s[i] in m1 and m1[s[i]] != t[i]) or (t[i] in m2 and m2[t[i]] != s[i]):
                return False
            m1[s[i]] = t[i]
            m2[t[i]] = s[i]
        return True
