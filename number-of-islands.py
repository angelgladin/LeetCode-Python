# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(grid, i+1, j)
                dfs(grid, i, j+1)
                dfs(grid, i-1, j)
                dfs(grid, i, j-1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans