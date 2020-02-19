# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        levels = []
        sublevel = []
        q = [root, None]
        while q:
            val = q.pop(0)
            if val == None:
                # If sublevel it's empty means that we've reach the end
                if sublevel: 
                    q.append(None)
                    levels.append(sublevel[:])
                    sublevel.clear()
            else:
                sublevel.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            
        return [x[-1] for x in levels]
