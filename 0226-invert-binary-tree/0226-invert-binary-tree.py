# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        if root is None:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
        '''

        if not root:
            return
        queue = []
        queue.append(root)

        while(queue):
            node = queue.pop(0)

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


