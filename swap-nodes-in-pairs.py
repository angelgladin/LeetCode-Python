# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next is not None and current.next.next is not None:
            p1 = current.next
            p2 = current.next.next
            
            p1.next = p2.next
            current.next = p2
            current.next.next = p1
            
            current = p1

        return dummy.next
