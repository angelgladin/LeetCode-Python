# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            return
        self.m = matrix
        
        c, r = len(self.m), len(self.m[0])
        
        dp = [[0]*r for _ in range(c)]
        dp[0][0] = self.m[0][0]
        
        for i in range(1, r):
            dp[0][i] = dp[0][i-1] + self.m[0][i]
        for i in range(1,c):
            dp[i][0] = dp[i-1][0] + self.m[i][0]
            
        for i in range(1, c):
            for j in range(1, r):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + self.m[i][j]
        
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.dp[row2][col2]
        if row1-1 >= 0 and col1-1 >= 0:
            ans += self.dp[row1-1][col1-1]
        if col1-1 >= 0:
            ans -= self.dp[row2][col1-1]
        if row1-1 >= 0:
            ans -= self.dp[row1-1][col2]
        return ans        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)