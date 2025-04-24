from collections import deque

def distanceK(root, target, k: int):
    ans = []
    parent = {}
    queue = deque([root])

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left.val] = node
            if node.right:
                queue.append(node.right)
                parent[node.right.val] = node


    visited = []
    queue.append(target)
    while queue:
        node = queue.pop()
        visited[node.val] = 1

        for _ in range(k):
            if node.left and node.left.val not in visited:
                queue.append(node.left)

            if node.right and node.right.val not in visited:
                queue.append(node.right)

            if node.val in parent and parent[node.val].val not in visited:
                queue.append(parent[node.val])

        k-=1

    while queue:
        node = queue.popleft()
        ans.append(node.val)

    return ans

