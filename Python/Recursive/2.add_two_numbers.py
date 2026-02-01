# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(a, b, carry):
            if not a and not b and not carry:
                return None
            
            val_a = 0 if not a else a.val
            val_b = 0 if not b else b.val

            sum = val_a + val_b + carry
            node = ListNode(sum % 10)
            new_carry = sum // 10
            node.next = helper(a.next if a else None, 
                               b.next if b else None, 
                               new_carry)

            return node
        
        return helper(l1,l2,0)
            

            

