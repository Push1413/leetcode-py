# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        my_queue = queue.Queue()
        my_queue.put(root)
        result = []

        while not my_queue.empty():
            level_size = my_queue.qsize()  # Get the number of nodes at the current level
            temp = []

            for _ in range(level_size):
                curr = my_queue.get()
                temp.append(curr.val)
                if curr.left:
                    my_queue.put(curr.left)
                if curr.right:
                    my_queue.put(curr.right)
            result.append(temp)
        return result
            




        