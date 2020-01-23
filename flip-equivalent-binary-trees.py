# 951. Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def f(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None or t1.val != t2.val:
                return False
            else:
                return (f(t1.left, t2.left) and f(t1.right, t2.right)) or \
                        (f(t1.left, t2.right) and f(t1.right, t2.left))
        
        return f(root1, root2)
