# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        intervals.sort(key=lambda x: x[0])
        for x in intervals:
            if not l:
                l.append(x)
            else:
                if l[-1][1] >= x[0]:
                    aux = l.pop()
                    aux[1] = max(x[1], aux[1])
                    l.append(aux)
                else:
                    l.append(x)
        return l
