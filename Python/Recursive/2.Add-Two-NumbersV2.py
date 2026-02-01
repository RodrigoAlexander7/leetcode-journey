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
        def helper(a,b,carry,iter):
            if not a and not b and not carry:  # if a and b not exist and not carry (cause else we need to continue adding) add nothing
                return None

            a = ListNode(0) if not a else a
            b = ListNode(0) if not b else b
            
            sum = a.val + b.val + carry     # calculate the sum of values
            iter.next = ListNode(sum % 10)  # the next node initialized
            new_carry = sum // 10           # the carry
            return helper(a.next,b.next,new_carry,iter.next)
        helper(l1,l2,0,iter)
        return centinel.next

            

            

