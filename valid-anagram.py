# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for x in s:
            d1[x] += 1
        for x in t:
            d2[x] += 1
        return d1 == d2
