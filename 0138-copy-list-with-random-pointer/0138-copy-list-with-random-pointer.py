"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head
        if head:
            while curr:
                hashmap[curr] = Node(curr.val)
                curr = curr.next
            curr = head
            while curr:
                newCopy = hashmap[curr]
                newCopy.next = hashmap.get(curr.next)
                newCopy.random = hashmap.get(curr.random)
                curr = curr.next
            return hashmap[head] 
        else:
            return None
        
        



        