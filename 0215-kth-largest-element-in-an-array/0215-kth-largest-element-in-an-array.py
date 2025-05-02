class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        ans = -1

        for i in range(n):
            heapq.heappush(heap,(-1*nums[i]))
        
        for i in range(k):
            ans = heapq.heappop(heap)
        
        return (-1 * ans)