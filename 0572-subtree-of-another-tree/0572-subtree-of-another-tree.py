# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                if root1.val == root2.val:
                    leftSide1 = root1.left
                    leftSide2 = root2.left

                    rightSide1 = root1.right
                    rightSide2 = root2.right
                   
                    return compare(leftSide1,leftSide2) and  compare(rightSide1,rightSide2)
                else:
                    return False
                
            else:
                return False
                
           
        def DFS(curr):
            if not curr:
                return False
            if curr.val == subRoot.val and compare(curr, subRoot):
                return True
            else:  
                return DFS(curr.left) or DFS(curr.right)
        
        if not subRoot:
            return True # if subroot is none, it is always a subtree
        if not root:
            return False # if root is none, and subroot is not, then it cannot be a subtree.

        return DFS(root)

        