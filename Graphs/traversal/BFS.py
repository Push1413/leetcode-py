from collections import deque
def bfs(adj):
    n = len(adj)
    q = deque()
    visited = [False] * n
    result = []
    q.append(0)
    visited[0] = True
    while q:
        pop = q.popleft()
        result.append(pop)

        for nei in adj[pop]:
            if not visited[nei]:
                q.append(nei)
                visited[nei] = True

    return result

if __name__=='__main__':
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(bfs(adj))