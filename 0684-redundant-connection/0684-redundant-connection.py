class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank= [0] * (n+1)

        def find(i):
            if parent[i]==i:
                return i
            return find(parent[i])
        
        def union(p1,p2):
            u1,u2 = find(p1),find(p2)
            if u1==u2:
                return False
            if rank[u1]<rank[u2]:
                parent[u1] = u2
                rank[u2] += rank[u1]
            else:
                parent[u2] = u1
                rank[u1] += rank[u2]
            return True
        

        for a,b in edges:
            if not union(a,b):
                return [a,b]


        