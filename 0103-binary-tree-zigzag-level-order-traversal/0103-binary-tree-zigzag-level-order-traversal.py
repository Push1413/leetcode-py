# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        left_To_Right = True
        if not root:
            return ans
        queue = deque([root])
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_To_Right:
                temp.reverse()
            ans.append(temp)
            left_To_Right = not left_To_Right
        return ans    