def coinChange(coins, amount):
  dp = [float("inf")] * (amount + 1)
  dp[0] = 0

  for i in range(1, amount+1):
    for coin in coins:
      if i - coin >= 0:
        # Checks all possible ways to make i using different coins.
        dp[i] = min(dp[i], 1 + dp[i - coin]) # This refers to the minimum number of coins needed to make the amount (i - coin). Since we're adding coin, we only need one more coin to form i, so we add 1:  

  if dp[amount] != float("inf"):
    return dp[amount]

  return -1


# T: O(N * M)    , N=amount, M=number of coins
# S: O(n)     , we just created dp array. Lenght is equal to amount

print(coinChange([1,2,5], 11))
