# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        w = defaultdict(int)
        i, j, n, ans = 0, 0, len(s), 0
        
        while j < n:
            w[s[j]] += 1
            while len(w) > k:
                c = s[i]
                if c in w:
                    w[c] -= 1
                    if w[c] == 0:
                        del w[c]
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        
        return ans
