class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        visited = [0] * n
        sum = 0
        adj_list = [[] for _ in range(n)]

        def getmanHattanDist(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p2[1]-p1[1])
        
        for i in range(n):
            for j in range(i + 1, n):
                distance = getmanHattanDist(points[i], points[j])
                adj_list[i].append((j, distance))
                adj_list[j].append((i, distance))
        
        size = len(adj_list)
        
        # w,destnode
        heap = [(0,0)]

        while heap:
            w1,n1 = heapq.heappop(heap)
            if not visited[n1]:
                visited[n1]=1
                sum +=w1
                for n2,w2 in adj_list[n1]:
                    heapq.heappush(heap,(w2,n2))
        return sum
    