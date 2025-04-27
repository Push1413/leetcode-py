# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def DFS(root):
            if not root:
                return 0
            
            maxleft = DFS(root.left)
            maxright = DFS(root.right)
            maxleft = max(maxleft,0)
            maxright = max(maxright,0)

            res[0] = max(res[0],root.val + maxright+ maxleft)

            return root.val + max(maxleft,maxright)
    
        DFS(root)    
        return res[0]      