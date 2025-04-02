"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}

        def DFS(original_node):
            if original_node in visited:
                return visited[original_node]

            copy_Node = Node(original_node.val)
            visited[original_node] = copy_Node

            for adj in original_node.neighbors:
                copy_Node.neighbors.append(DFS(adj))
            
            return copy_Node
        
    
        return DFS(node)


        
        