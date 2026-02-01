# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root: Optional[TreeNode], path:str):
            if not root:
                return
            
            path = str(root.val) if path == '' else  path + '->' + str(root.val)

            if not root.right and not root.left:
                res.append(path)
                return
            
            dfs(root.right, path)
            dfs(root.left, path)
        dfs(root,'')
        return res