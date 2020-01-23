# 66. Plus One
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            aux = digits[i]+carry
            if aux > 9:
                carry = 1
                aux = 0
            else:
                carry = 0
            digits[i] = aux
            
        if carry == 1:
            digits.insert(0, 1)
        return digits