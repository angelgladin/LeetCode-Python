# 247. Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def backtrack(low, high, buffer, mapping, ans):
            if low > high:
                ans.append(''.join(buffer))
                return
            
            for k in mapping:
                if low == high and k in ('6','9',):
                    continue
                if low < high and low == 0 and k == '0':
                    continue
                buffer[low] = k
                buffer[high] = mapping[k]
                backtrack(low+1, high-1, buffer, mapping, ans)

        mapping = { '0' : '0', '1': '1', '6' : '9', '8' : '8', '9' : '6' }
        buffer = [None]*n
        ans = []
        backtrack(0, n-1, buffer, mapping, ans)
        return ans
