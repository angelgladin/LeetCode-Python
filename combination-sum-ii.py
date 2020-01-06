# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(l, n, idx, aux, current_sum, k, ans):
            if current_sum > k:
                return
            if current_sum == k:
                ans.add(tuple(sorted(aux)))
                return
            for i in range(idx, n):
                aux.append(l[i])
                backtrack(l, n, i+1, aux, current_sum+l[i], k, ans)
                aux.pop()
        
        ans = set()
        backtrack(candidates, len(candidates), 0, [], 0, target, ans)
        return list(ans)
