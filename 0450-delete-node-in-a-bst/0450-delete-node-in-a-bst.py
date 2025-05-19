# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        curr = root
        l = root.left
        r = root.right

        # get highest from left
        while l.right:
            l = l.right
        l.right = r
        return curr.left
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==key:
            return self.helper(root)
    
        curr = root
        while root:
            if key<root.val:
                if root.left and root.left.val==key:
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val==key:
                    root.right = self.helper(root.right)
                    break
                root = root.right 
        return curr