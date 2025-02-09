class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        maxRight = [0] * n
        maxLeft = [0] * n
        ans =0
        maxLeft[0] = height[0]
        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1],height[i]) 
        
        maxRight[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i])
        
        for i in range(n):
            min_height = min(maxRight[i],maxLeft[i])
            curr_height = height[i]

            capacity = min_height - curr_height
            if capacity > 0:
                ans +=capacity
            
        return ans


        