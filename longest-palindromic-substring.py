# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
        for d in range(1, n):
            for i in range(n-d):
                j = d+i
                if s[i] == s[j]:
                    if j-i == 1:
                        dp[i][j] = True
                        ans = s[i:j+1]
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > len(ans):
                            ans = s[i:j+1]
        return ans
