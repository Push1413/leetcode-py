class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (dist, point)
        heap = []
        ans = []
        def findDist(point1):
            diff1 = point1[0]- 0
            diff2 = point1[1]- 0
            sum1 = diff1*diff1 + diff2*diff2
            dist = math.sqrt(sum1)
            return (-1 * dist)
        
        for i in range(len(points)):
            dist = findDist(points[i])
            t1 = (dist, points[i])
            heapq.heappush(heap,t1)
            if len(heap)>k:
                heapq.heappop(heap)
        
        for i in range(len(heap)):
            dist,point = heap[i]
            ans.append(point)
        
        return ans
        