# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        p = head
        mapping = dict()
        
        while p:
            mapping[p] = Node(p.val)
            p = p.next
        
        p = head
        
        while p:
            aux = mapping[p]
            aux.next = mapping.get(p.next, None)
            aux.random = mapping.get(p.random, None)
            
            p = p.next
            
        return mapping[head]
