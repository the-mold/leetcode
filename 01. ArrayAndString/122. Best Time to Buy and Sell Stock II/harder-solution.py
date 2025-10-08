#Note: whenever next price is higher then the current one, buy now and sell the next day.
# You do not need to wait till price reaches its maximum. All these one day profits will add up to the profit, if you would wait for the day with max selling price.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        
        return profit

# T:O(n)
# S:O(1)
