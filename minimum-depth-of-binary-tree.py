# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution:    
    def minDepth(self, root: TreeNode) -> int:
        def is_leaf(node):
            if node is not None and node.left is None and node.right is None:
                return True
            return False
        
        if root is None:
            return 0
        stack = []
        ans = math.inf
        stack.append((root, 1,))
        while stack:
            node, depth = stack.pop()
            if is_leaf(node):
                ans = min(ans, depth)
            if node.left is not None:
                stack.append((node.left, depth+1,))
            if node.right is not None:
                stack.append((node.right, depth+1,))
        return ans            
