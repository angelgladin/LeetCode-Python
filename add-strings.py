# 415. Add Strings
# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        i, j = n1-1, n2-1
        carry = 0
        ans = []
        while i >= 0 or j >= 0:
            s = carry
            if i >= 0:
                s += int(num1[i])
                i -= 1
            if j >= 0:
                s += int(num2[j])
                j -= 1

            if s > 9:
                carry = 1
            else:
                carry = 0
            
            ans.append(str(s%10))

        if carry == 1:
            ans.append('1')
        
        return ''.join(ans[::-1])
