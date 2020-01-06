# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, N: int) -> bool:
        invalid = ['2','3','4','5','7']
        s = str(N)
        for x in s:
            if x in invalid:
                return False
        m = dict()
        m['0'] = '0'
        m['1'] = '1'
        m['6'] = '9'
        m['8'] = '8'
        m['9'] = '6'
        aux = ''
        for x in s[::-1]:
            aux += m[x]
        return s != aux
