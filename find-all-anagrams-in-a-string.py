# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def equals(w1, w2, n):
            for i in range(26):
                if w1[i] != w2[i]:
                    return False
            return True
        
        if not s or len(s) < len(p):
            return []

        ns, np = len(s), len(p)
        w1, w2 = [0]*26, [0]*26
        ans = []
        idx = lambda x: ord(x) - ord('a')
        
        for i in range(np):
            w1[idx(s[i])] += 1
            w2[idx(p[i])] += 1
        
        for i in range(ns-np+1):
            if equals(w1, w2, np):
                ans.append(i)
            w1[idx(s[i])] -= 1
            if i+np < ns:
                w1[idx(s[i+np])] += 1
        
        return ans
