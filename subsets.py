# 78. Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(l, idx, aux, ans):
            ans.append(aux[:])
            for i in range(idx, len(l)):
                aux.append(l[i])
                backtrack(l, i+1, aux, ans)
                aux.pop()
        
        ans = []
        backtrack(nums, 0, [], ans)
        return ans