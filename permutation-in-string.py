# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        def check(l1, l2):
            for i in range(26):
                if l1[i] != l2[i]:
                    return False
            return True
        
        w1 = [0]*26
        w2 = [0]*26
        for i in range(n1):
            w1[ord(s1[i]) - ord('a')] += 1
            w2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(n2-n1):
            if check(w1, w2):
                return True
            w2[ord(s2[i+n1]) - ord('a')] += 1
            w2[ord(s2[i]) - ord('a')] -= 1
        # Check the last chunk since the for loop goes from (0, n2-n1) and there's
        # one missing chunk to check their occurrences.
        return check(w1, w2)
