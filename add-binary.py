# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            n = carry
            if i >= 0:
                n += int(a[i])
            if j >= 0:
                n += int(b[j])
                
            if n == 3:
                ans += '1'
                carry = 1
            elif n == 2:
                ans += '0'
                carry = 1
            elif n == 1:
                ans += '1'
                carry = 0
            elif n == 0:
                ans += '0'
                carry = 0
            i -= 1
            j -= 1
        if carry == 1:
            ans += '1'
        
        return ans[::-1]
