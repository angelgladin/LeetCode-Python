# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepest = (root, 0,)
        d = dict()
        s = [(root, 0,)]
        while s:
            x_node, x_depth = s.pop()
            d[x_node.val] = x_depth
            if x_depth > deepest[1]:
                deepest = (x_node, x_depth,)
            if x_node.left:
                s.append((x_node.left, x_depth+1,))
            if x_node.right:
                s.append((x_node.right, x_depth+1,))
        
        def ans(node):
            if node is None or d[node.val] == deepest[1]:
                return node
            l, r = ans(node.left), ans(node.right)
            if l and r:
                return node
            elif l and not r:
                return l
            return r
        
        return ans(root)
