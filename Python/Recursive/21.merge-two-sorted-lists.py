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
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list2, list1.next)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

        