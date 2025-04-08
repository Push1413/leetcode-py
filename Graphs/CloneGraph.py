class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    visited = {}

    def DFS(root):
        if root in visited:
            return visited[root]

        new_node = Node(root.val)
        visited[root] = new_node

        for nei in root.neighbors:
            if nei not in visited:
                new_node.neighbors.append(DFS(nei))

        return new_node

    return DFS(node)

