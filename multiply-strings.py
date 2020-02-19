# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        ans = [0]*(n+m)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                prod = int(num1[i]) * int(num2[j])
                sum_ = ans[i+j+1] + prod
                carry = sum_ // 10
                ans[i+j+1] = sum_%10
                ans[i+j] += carry
        s = ''
        for x in ans:
            if len(s) != 0 or x != 0:
                s += str(x)
        if len(s) == 0:
            return '0'
        else:
            return s
