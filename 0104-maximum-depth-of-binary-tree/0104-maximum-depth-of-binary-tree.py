# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mx =0
    def find(self,root: Optional[TreeNode],x):
        if root ==None:
            self.mx = max(self.mx,x)
            return
        self.find(root.left,x+1)
        self.find(root.right,x+1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.find(root,0)
        return self.mx

    
        