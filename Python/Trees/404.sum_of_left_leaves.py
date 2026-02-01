from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper( root:TreeNode, isLeft: bool):
            if not root:
                return 0
            if not root.right and not root.left:
                return root.val if isLeft else 0

            left_side = root.left if root.left else TreeNode()        
            right_side = root.right if root.right else TreeNode()        

            return helper(left_side, True) + helper(right_side, False)
        
        if not root:
            return 0
        return helper(root, False)