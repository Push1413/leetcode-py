import heapq
from collections import defaultdict

def dijkstra(graph, n, start):
    adj_set = defaultdict(list)
    for u,v,w in graph:
        adj_set[u].append((w,v))
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = [(0,start)]

    while heap:
        w1,n1 = heapq.heappop(heap)
        if w1 > dist[n1]:
            continue
        for w2,n2 in adj_set[n1]:
            if dist[n2]> w2+w1:
                dist[n2] = min(dist[n2], w1+w2)
                heapq.heappush(heap,(dist[n2],n2))

    return dist[1:]

if __name__ == '__main__':
    graph = [
        (1, 2, 2),
        (1, 3, 4),
        (2, 3, 1),
        (2, 4, 7),
        (3, 5, 3),
        (4, 6, 1),
        (5, 4, 2),
        (5, 6, 5)
    ]
    n = 6
    start = 1
    distances = dijkstra(graph, n, start)
    print("Shortest distances from node", start, ":", distances)