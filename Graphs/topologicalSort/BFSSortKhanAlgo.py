from collections import deque
def topoSort(V, edges):
    adj = [[] for _ in range(V)]
    inDegree = [0] * V
    result = []
    for u,v in edges:
        adj[u].append(v)
        inDegree[v] +=1

    q = deque([i for i in range(V) if inDegree[i]==0])

    while q: # BFS
        pop = q.popleft()
        result.append(pop)

        for nei in adj[pop]:
            inDegree[nei] -= 1
            if inDegree[nei]==0:
                q.append(nei)

    if len(result)!=V: # cycle detected
        return []
    return result

if __name__=='__main__':
    V = 4
    edges= [[3, 0], [1, 0], [2, 0]]
    print(topoSort(V,edges))