# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def aux_valid(i, j, s):
            while i <= i + (j-i)//2:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        n = len(s)
        i, j = 0, n-1
        while i < n//2:
            if s[i] != s[j]:
                return aux_valid(i+1, j, s) or aux_valid(i, j-1, s)
            i += 1
            j -= 1
        return True
