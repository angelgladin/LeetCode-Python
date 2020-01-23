# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math
        points.sort(key=lambda x: math.hypot(x[0], x[1]))
        return points[:K]
