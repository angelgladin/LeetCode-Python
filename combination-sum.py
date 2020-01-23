# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(l, k, s, idx, n, aux, ans):
            if s == k:
                ans.append(aux[:])
            elif s > k:
                return
            for i in range(idx, n):
                aux.append(l[i])
                backtrack(l, k, s+l[i], i, n, aux, ans)
                aux.pop()
        
        ans = []
        backtrack(candidates, target, 0, 0, len(candidates), [], ans)
        return ans
