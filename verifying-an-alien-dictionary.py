# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = { c: chr(i+ord('a')) for (i,c,) in enumerate(order) }
        n = len(words)
        for i in range(n-1):
            w1 = ''.join([mapping[x] for x in words[i]])
            w2 = ''.join([mapping[x] for x in words[i+1]])
            if w1 > w2:
                return False
        return True
