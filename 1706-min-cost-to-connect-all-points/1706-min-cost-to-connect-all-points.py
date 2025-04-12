class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<2:
            return 0

        def ManhattanDist(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        adj_list = [[] for _ in range(n)]
        sum = 0
        visited = [False] * n
        # weight, node
        minHeap = [(0,0)]

        for i in range(n):
            for j in range(i+1,n):
                dist = ManhattanDist(points[i],points[j])
                adj_list[i].append((dist, j))
                adj_list[j].append((dist,i))

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if not visited[n1]:
                visited[n1] = True
                sum +=w1
                for w2,n2 in adj_list[n1]:
                    if not visited[n2]:
                        heapq.heappush(minHeap,(w2,n2))

        return sum
        