from collections import deque
def isBipartite(graph):
    n = len(graph)
    color = [-1] * n

    for i in range(n):
        if color[i]==-1:
            queue = deque([i])
            color[i] = 0

            while queue:
                item = queue.popleft()
                for nei in graph[item]:
                    if color[nei]==-1:
                        color[nei] = 1 - color[item]  # Assign opposite color
                        queue.append(nei)
                    elif color[nei] == color[item]:
                        return False
    return True

if __name__ =='__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(isBipartite(graph))