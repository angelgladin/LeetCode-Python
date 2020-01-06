# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.ans = 0
        def f(v):
            if v is None:
                return 0
            l_depth = f(v.left)
            r_depth = f(v.right)
            self.ans = max(self.ans, l_depth + r_depth + 1)
            return max(l_depth, r_depth) + 1
        f(root)
        return self.ans-1
