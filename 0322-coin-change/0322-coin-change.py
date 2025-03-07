class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #create dp array of min no of coins needed for the amount = i
        # set to infinity or amount +1. 
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        
        return dp[amount] if dp[amount]!=(amount+1) else -1





        