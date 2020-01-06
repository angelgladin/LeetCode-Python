# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1, stack2 = [], []
        i, j = 0, 0
        n1, n2, = len(S), len(T)

        while i<n1:
            if S[i] == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(S[i])
            i += 1

        while j<n2:
            if T[j] == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(T[j])
            j += 1

        return stack1 == stack2
