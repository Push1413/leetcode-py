class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * (n+1)

        minCost[0] = 0
        minCost[1] = 0

        for i in range(2,n+1):
            minCost[i] = min((cost[i-1]+minCost[i-1]),(cost[i-2]+minCost[i-2]))
        
        return minCost[-1]

        