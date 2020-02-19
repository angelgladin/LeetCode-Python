# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        sign = 1
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
        
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        ans = 0
        
        while i < n and s[i].isdigit():
            ans = (ans * 10) + int(s[i])
            i += 1
            
        ans *= sign
        
        min_bound = -1 << 31
        max_bound = (1 << 31)-1
        
        if ans > max_bound:
            return max_bound
        elif ans < min_bound:
            return min_bound
        return ans
