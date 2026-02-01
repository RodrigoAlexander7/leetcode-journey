# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 : 
            return None
        # if len(nums) == 1:
        #     return TreeNode(nums[0])

        idx = len(nums)//2 
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[0:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root
        
        