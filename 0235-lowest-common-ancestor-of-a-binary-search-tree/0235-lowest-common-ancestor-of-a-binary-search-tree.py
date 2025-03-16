# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFSSearch(root, target):
            path = []
            curr = root
            while curr:
                path.append(curr)
                if target.val < curr.val:
                    curr = curr.left
                elif target.val > curr.val:
                    curr = curr.right
                else:
                    break
            return path 


        pList = DFSSearch(root,p)
        qList = DFSSearch(root,q)
        lca = None

        for u,v in zip(pList,qList):
            if u == v:
                lca = v
            else:
                break

        return lca



        