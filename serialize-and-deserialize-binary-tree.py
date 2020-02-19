# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root, ans):
            if root is None:
                ans.append('null')
            else:
                ans.append(str(root.val))
                preorder(root.left, ans)
                preorder(root.right, ans)
        
        ans = []
        preorder(root, ans)
        s = '[' + ','.join(ans) + ']'
        return s
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder(data):
            if data[0] == 'null':
                data.pop(0)
                return None
            else:
                root = TreeNode(data[0])
                data.pop(0)
                root.left = preorder(data)
                root.right = preorder(data)
                return root
        
        aux = data[1:-1].split(',')
        return preorder(aux)
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
