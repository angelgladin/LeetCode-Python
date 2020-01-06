# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p = ListNode(-1)
        ans = p
        while l1 is not None or l2 is not None:
            aux = carry
            if l1 is not None:
                aux += l1.val
                l1 = l1.next
            if l2 is not None:
                aux += l2.val
                l2 = l2.next
            if aux > 9:
                carry = 1
            else:
                carry = 0
            aux_node = ListNode(aux%10)
            p.next = aux_node
            p = p.next
        if carry == 1:
            p.next = ListNode(1)
        return ans.next
