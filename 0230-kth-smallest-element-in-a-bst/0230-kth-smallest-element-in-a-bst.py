# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count =0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inOrderTra(curr,k):
            if not curr:
                return 0
            leftC = inOrderTra(curr.left,k)
            print(curr.val)
            self.count +=1
            if self.count == k:
                return curr.val
            rightC = inOrderTra(curr.right,k)
            return leftC + rightC

        if not root:
            return 0
        
        return inOrderTra(root,k)

        

        