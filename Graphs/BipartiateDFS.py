def isBipartite(graph):
    n = len(graph)
    color = [-1] * n
    # default -1. color-0,1

    def DFS(node,c):
        color[node]= c
        for nei in graph[node]:
            if color[nei]==-1:
                if not DFS(nei, 1 - c):
                    return False
            elif color[nei] == c:
                return False
        return True

    for i in range(n):
        if color[i]==-1:
            if not DFS(i, 0):
                return False

    return True

if __name__ =='__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(isBipartite(graph))