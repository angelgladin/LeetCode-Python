# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        
        m = dict()
        m['2'] = ['a', 'b', 'c']
        m['3'] = ['d', 'e', 'f']
        m['4'] = ['g', 'h', 'i']
        m['5'] = ['j', 'k', 'l']
        m['6'] = ['m', 'n', 'o']
        m['7'] = ['p', 'q', 'r', 's']
        m['8'] = ['t', 'u', 'v']
        m['9'] = ['w', 'x', 'y', 'z']
        
        def combinations(digits, m, idx, n, aux, ans):
            if idx == n:
                ans.append(''.join(aux[:]))
                aux.clear
            else:
                for x in m[digits[idx]]:
                    aux.append(x)
                    combinations(digits, m, idx+1, n, aux, ans)
                    aux.pop()
        
        ans = []
        combinations(digits, m, 0, len(digits), [], ans)
        return ans
