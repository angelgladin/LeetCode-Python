# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        f = {}
        q = [node]
        
        f[node] = Node(node.val, [])
        
        while q:
            u = q.pop(0)
            for v in u.neighbors:
                if v not in f:
                    f[v] = Node(v.val, [])
                    q.append(v)
                f[u].neighbors.append(f[v])
        
        return f[node]
