# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m):
            for i in range(len(m)):
                for j in range(i+1, len(m)):
                    tmp = m[i][j]
                    m[i][j] = m[j][i]
                    m[j][i] = tmp
                    
            
        def vertical_reverse(m):
            for i in range(len(m)):
                m[i].reverse()
        
        transpose(matrix)
        vertical_reverse(matrix)
