# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        aux = ''
        for x in s:
            if x.isalpha():
                aux += x.lower()
            elif x.isdigit():
                aux += x
        i, j = 0, len(aux)-1
        while i < j:
            if aux[i] != aux[j]:
                return False
            i += 1
            j -= 1
        return True
