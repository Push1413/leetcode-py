def findRedundantConnection(edges):
    v = len(edges)
    # starts from 1
    parent = [i for i in range(v+1)]

    def find(i):
        if parent[i]==i:
            return i
        return find(parent[i])

    def union(n1,n2):
        p1,p2 = find(n1), find(n2)
        if p1==p2:
            return False
        # random assign parent to any node
        parent[p1] = p2
        return True

    for u,v in edges:
        if not union(u,v):
            return [u,v]

if __name__=='__main__':
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(findRedundantConnection(edges))
