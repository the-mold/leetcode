class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peak = prices[0]
        low = prices[0]

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < peak:
                profit += peak-low
                peak = prices[i]
                low = prices[i]
            elif prices[i] >= peak:
                peak = prices[i]

        # in the end, you must do one more transaction. It happens when
        # prices go up and never down. 
        profit += peak-low

        return profit
      
#T:O(n)
#S:O(1)
