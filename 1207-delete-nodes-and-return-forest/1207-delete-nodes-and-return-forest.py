# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        deleteSet = set(to_delete)

        def DFS(node,is_root):
            if not node:
                return None
            
            deleted = node.val in deleteSet

            node.left = DFS(node.left,deleted)
            node.right = DFS(node.right,deleted)

            if deleted:
                return None
            elif is_root:
                result.append(node)
                return node
            else:
                return node
        
        DFS(root,True)
        
        return result
            

               
                

        