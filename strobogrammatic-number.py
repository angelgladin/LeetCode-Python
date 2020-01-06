# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = dict()
        d['0'] = '0'
        d['1'] = '1'
        d['6'] = '9'
        d['8'] = '8'
        d['9'] = '6'
        
        i, j = 0, len(num)-1
        while i <= j:
            if num[i] not in d or num[j] not in d or num[i] != d[num[j]] or num[j] != d[num[i]]:
                return False
            i += 1
            j -= 1
        return True
