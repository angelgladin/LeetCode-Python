# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        aux = ListNode(-1)
        aux.next = head
        ptr1 = ptr2 = aux
        
        for _ in range(n+1):
            ptr2 = ptr2.next
            
        while ptr2 is not None:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr1.next = ptr1.next.next
        
        return aux.next
