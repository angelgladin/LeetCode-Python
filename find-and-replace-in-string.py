# 833. Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ''
        d = dict()
        for i in range(len(indexes)):
            if S.startswith(sources[i], indexes[i]):
                d[indexes[i]] = (targets[i], len(sources[i]),)
        i = 0
        n = len(S)
        while i < n:
            if i in d:
                ans += d[i][0]
                i += d[i][1]
            else:
                ans += S[i]
                i += 1
        return ans
