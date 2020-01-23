# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(l, n, cache, aux, res):
            if len(aux) == n:
                res.add(tuple(aux))
                return
            for i in range(n):
                if not cache[i]:
                    aux.append(nums[i])
                    cache[i] = True
                    backtrack(l, n, cache, aux, res)
                    aux.pop()
                    cache[i]= False
        ans = set()
        n = len(nums)
        cache = [False]*n
        backtrack(nums, n, cache, [], ans)
        return list(ans)
