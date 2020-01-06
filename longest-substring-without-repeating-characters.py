# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        window = set()
        i, j = 0, 0
        while i < n and j < n:
            if s[j] not in window:
                window.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                window.remove(s[i])
                i += 1
        return ans
