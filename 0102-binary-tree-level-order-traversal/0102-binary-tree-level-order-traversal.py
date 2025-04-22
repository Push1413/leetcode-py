# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        queue = deque([root])

        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    temp.append(curr.right.val)
            if len(temp)!=0:
                ans.append(temp)   
        return ans
                    