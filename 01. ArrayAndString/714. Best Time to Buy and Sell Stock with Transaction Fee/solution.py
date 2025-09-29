from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Calculates the maximum profit with a transaction fee using a dynamic programming approach.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize states before the first day.
        # 'free': 0 profit if we don't hold any stock.
        # 'hold': Negative price of the first stock, as if we bought it on day 0.
        free = 0
        hold = -prices[0]

        # Iterate through the prices starting from the second day.
        for i in range(1, len(prices)):
            price = prices[i]
            
            # Keep the previous 'free' value to use in the 'hold' calculation.
            prev_free = free
            
            # The new 'free' state is the max of:
            # 1. Not doing anything (staying free).
            # 2. Selling the stock we were holding.
            free = max(free, hold + price - fee)
            
            # The new 'hold' state is the max of:
            # 1. Not doing anything (continuing to hold).
            # 2. Buying a stock today (from a 'free' state).
            hold = max(hold, prev_free - price)
            
        # On the last day, the maximum profit must be when we are 'free' (not holding any stock).
        return free

#T:O(n)
#S:O(1)

#Intuition
# The key is to track the maximum profit you could have at the end of each day in two possible states:

# hold: The maximum profit if you are holding a share of stock.
# free: The maximum profit if you are not holding a share (i.e., you are "free" to buy).
# The Logic
# We can iterate through the daily prices and update these two states based on the actions we can take: buy, sell, or do nothing.

# For each day i with price = prices[i]:

# To update hold:
# You could have been holding from the previous day (do nothing). The profit is still the old hold.
# You could have been free yesterday and decided to buy today. The profit would be free - price.
# So, the new hold is the maximum of these two options: max(hold, free - price).
# To update free:
# You could have been free yesterday and decided to do nothing. The profit is still the old free.
# You could have been holding a stock yesterday and decided to sell today. The profit would be hold + price - fee.
# So, the new free is the maximum of these two options: max(free, hold + price - fee).
# At the end of all the days, the maximum possible profit will be when you are not holding any stock, which is the final free value.