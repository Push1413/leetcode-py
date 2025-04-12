from collections import defaultdict
def kruskalAlgo(n,adj):
    parent = [i for i in range(n)]

    def NonOptimisedFind(p1):
        if parent[p1]==p1:
            return p1
        return parent[p1]

    def find(p1):
        if parent[p1]!=p1:
            parent[p1] = find(parent[p1])
        return parent[p1]

    def union(p1,p2):
        u,v = find(p1), find(p2)
        if u==v:
            return False
        parent[p1] = p2
        return True

    edges = []
    visited = set()  # to track visited (u,v) pairs

    for u in adj:
        for v, w in adj[u]:
            if (v, u) not in visited:  # avoid duplicates
                edges.append((w, u, v))
                visited.add((u, v))

    # Sort edges by weight
    edges.sort()

    mst = []
    total_cost = 0

    for w,u,v in edges:
        if union(u,v):
            mst.append((u, v, w))
            total_cost += w
            if len(mst) == n - 1:
                break
                
    return total_cost, mst

if __name__=='__main__':
    n = 5
    adj = defaultdict(list)
    #srcNode:[(destNode,weight)]
    adj[0].append((1,2))
    adj[0].append((2,1))
    adj[1].append((0,2))
    adj[1].append((2,1))
    adj[2].append((0,1))
    adj[2].append((1,1))
    adj[2].append((4,2))
    adj[2].append((3,2))
    adj[3].append((4,1))
    adj[3].append((2,2))
    adj[4].append((2,2))
    adj[4].append((3,1))
    print(kruskalAlgo(n,adj))

