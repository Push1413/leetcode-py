# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def DFS(p1,q1):
            if not p1 and not q1:
                return True
            elif p1 and q1:
                if p1.val !=q1.val:
                    return False
                else:
                    return DFS(p1.left,q1.left)and DFS(p1.right,q1.right)
            else:
                return False
        
        return DFS(p,q)

        