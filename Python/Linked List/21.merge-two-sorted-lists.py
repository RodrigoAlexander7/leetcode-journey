#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
head = L1[i]

current = a -> L1[i] 
a -> L1[i] # head a
b -> L2[j] # head b
"""
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #using centinel node
        centinel = ListNode() # store a reference to the head
        tail = centinel # allways represent the las element

        a, b = list1, list2

        while a and b:
            if a.val < b.val:
                tail.next = a       # a is the new last element (insert a)
                a = a.next          # advance a pointer's  
            else:
                tail.next = b 
                b = b.next          # advance b pointer's
            tail = tail.next        # update the last element (the last inserted)


        tail.next = a if a else b
        return centinel.next