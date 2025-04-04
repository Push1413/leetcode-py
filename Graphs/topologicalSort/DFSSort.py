def getAdjFromEdges(edges,V):
    adj = [[] for _ in range(V)]
    for u,v in edges:
        adj[u].append(v)
    print(adj)
    return adj

def topoSort(V, edges):
    adj = getAdjFromEdges(edges, V)
    visited = [False] * V
    result = []
    stack = []

    def DFS(node):
        visited[node] = True

        for nei in adj[node]:
            if not visited[nei]:
                DFS(nei)
        stack.append(node)

    for i in range(V):
            if not visited[i]:
                DFS(i)

    while stack:
        result.append(stack.pop())

    return result

if __name__=='__main__':
    V = 4
    edges= [[3, 0], [1, 0], [2, 0]]
    print(topoSort(V,edges))
