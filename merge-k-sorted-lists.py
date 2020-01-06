# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        
        setattr(ListNode, '__lt__', lambda self, other: self.val < other.val)
        
        q = PriorityQueue()
        
        for x in lists:
            if x:
                q.put(x)
                
        head = ptr = ListNode(-1)
        
        while not q.empty():
            aux = q.get()
            ptr.next = ListNode(aux.val)
            if aux.next is not None:
                q.put(aux.next)
            ptr = ptr.next
        
        return head.next
