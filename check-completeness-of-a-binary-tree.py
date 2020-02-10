# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = [root]
        while q and q[0] is not None:
            x = q.pop(0)
            q.append(x.left)
            q.append(x.right)
        while q:
            x = q.pop(0)
            if x is not None:
                return False
        return True
