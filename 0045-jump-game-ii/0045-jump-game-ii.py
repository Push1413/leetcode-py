class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        dp = [float('inf')] * (n)
        dp[0] = 0

        for i in range(n):
            for j in range(i+1,min(i+1+nums[i],n)):
                dp[j] = min(dp[j], dp[i]+1)
        
        return dp[n-1] if dp[n - 1] != float('inf') else -1



        