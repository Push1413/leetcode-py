class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        heap = []
        for i in range(len(stones)):
            weight = -1 * stones[i]
            heapq.heappush(heap,weight)
        
        while len(heap)>1: 
            stone1 = -1 * (heapq.heappop(heap)) 
            stone2 = -1 * (heapq.heappop(heap))
            print(stone1)
            print(stone2)
            if stone1==stone2:
                continue
            elif stone1>stone2:
                stone1 = stone1-stone2
                heapq.heappush(heap, (-1 * stone1))
            else:
                stone1 = stone2- stone1
                heapq.heappush(heap,(-1 * stone1))
        
        return (-1 * heap[0]) if heap else 0        