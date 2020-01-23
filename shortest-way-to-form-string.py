# 1055. Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t, n_t, ans = 0, len(target), 0
        while t < n_t:
            t_aux = t
            for x in source:
                if t < n_t and x == target[t]:
                    t += 1
            if t_aux == t:
                return -1
            ans += 1
        return ans
