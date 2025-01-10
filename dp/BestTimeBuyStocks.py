#121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    minVal = max(prices)
    profit =0

    for i in prices:
        minVal = min(minVal, i)
        profit = max(profit, i-minVal)
    return profit

if __name__ == '__main__':
    num = [7,1,5,3,6,4]
    print(maxProfit(num))