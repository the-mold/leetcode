class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change(amount, coins, 0, {})
        
    def _change(self, amount, coins, idx, memo): 
        key = (amount, idx)
        if key in memo:
            return memo[key]

        if amount == 0:
            return 1

        if idx >= len(coins):
            return 0

        total = 0
        coin = coins[idx]
        for qty in range(0, (amount // coin) + 1):
            remainder = amount - (coin * qty)
            total += self._change(remainder, coins, idx+1, memo)
        
        memo[key] = total
        return total

# Variables:
# n = amount
# a = number of coins

#T:O(n*a)
#S:O(n*a)