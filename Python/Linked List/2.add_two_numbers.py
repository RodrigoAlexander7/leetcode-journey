# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        centinel = ListNode()
        iter = centinel
        carry = 0
        while l1 or l2 or carry:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            sum = val_l1 + val_l2 + carry
            iter.next = ListNode(sum % 10)
            carry = sum // 10

            iter = iter.next
            l1 = l1.next if l1 else l1
            l2= l2.next if l2 else l2
        return centinel.next
            

