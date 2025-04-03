def dfs(adj):
    n = len(adj)
    visited = [False] * n
    result = []

    def DFSHelper(node):
        visited[node] = True
        result.append(node)

        for nei in adj[node]:
            if not visited[nei]:
                DFSHelper(nei)

    DFSHelper(0)
    return result

if __name__=='__main__':
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(dfs(adj))

