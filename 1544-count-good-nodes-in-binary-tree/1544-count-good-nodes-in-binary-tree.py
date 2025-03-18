# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def traverse(curr, currMax):
            if not curr:
                return 0
            count =0
            if curr.val >= currMax:
                count = 1
                currMax = curr.val
            
            leftCount = traverse(curr.left, currMax)
            rightCount = traverse(curr.right, currMax)

            return count + leftCount + rightCount

        return traverse(root,root.val)
            
        