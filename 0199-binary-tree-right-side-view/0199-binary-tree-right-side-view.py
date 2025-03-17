# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        my_queue = queue.Queue()
        my_queue.put(root)

        while not my_queue.empty():
            size = my_queue.qsize()
            rightMost = None
            
            for _ in range(size):
                curr = my_queue.get()
                rightMost = curr
                if curr.left:
                    my_queue.put(curr.left)
                if curr.right:
                    my_queue.put(curr.right)
            if rightMost:
                ans.append(rightMost.val)
        return ans
            
           
            



        