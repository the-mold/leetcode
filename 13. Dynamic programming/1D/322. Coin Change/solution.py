def coinChange(coins, amount):
  dp = [float("inf")] * (amount + 1)  # [0......amount]
  dp[0] = 0 # to build amount of 0 we need 0 coins.

  for a in range(amount + 1):
    for coin in coins:
        if a - coin >= 0: # check if amount a could be built with the coin
            # For each coin that can build the amount a, update the soution in dp[a].
            # Solution is either previous value of dp[a] or a lower new value of 1+dp[a-coin].
            # 1 means that we add one coin(that is being checked) and add the number of coins that we need to
            # build the remainder. See step-by-step below. 
            dp[a] = min(dp[a], 1 + dp[a - coin])

  if dp[amount] != float("inf"):
    return dp[amount]

  return -1


# T: O(N * M)    , N=amount, M=number of coins
# S: O(n)     , we just created dp array. Lenght is equal to amount



print(coinChange([1,2,5], 11))


# The Loop Logic
# This is where we fill our dp array with answers, from the bottom up.

# python
# for a in range(1, amount + 1):
#     for coin in coins:
#         if a - coin >= 0:
#             dp[a] = min(dp[a], 1 + dp[a - coin])
# Let's trace this with an example: coins = [1, 3, 4] and amount = 6. Our dp array starts as: [0, inf, inf, inf, inf, inf, inf]

# Outer Loop: for a in range(1, amount + 1)
# This loop iterates through all the amounts we want to solve for, from 1 up to 6.

# a = 1: How to make 1?
# Try coin = 1: 1 - 1 >= 0. Possible. The cost is 1 + dp[1-1] which is 1 + dp[0] = 1 + 0 = 1. So, dp[1] becomes min(inf, 1) = 1.
# Try coin = 3: 1 - 3 < 0. Not possible.
# Try coin = 4: 1 - 4 < 0. Not possible.
# Result: dp is now [0, 1, inf, inf, inf, inf, inf]
# a = 2: How to make 2?
# Try coin = 1: 2 - 1 >= 0. Possible. Cost is 1 + dp[2-1] = 1 + dp[1] = 1 + 1 = 2. So, dp[2] becomes min(inf, 2) = 2.
# Result: dp is now [0, 1, 2, inf, inf, inf, inf]
# a = 3: How to make 3?
# Try coin = 1: 3 - 1 >= 0. Possible. Cost is 1 + dp[3-1] = 1 + dp[2] = 1 + 2 = 3. dp[3] is now 3.
# Try coin = 3: 3 - 3 >= 0. Possible. Cost is 1 + dp[3-3] = 1 + dp[0] = 1 + 0 = 1. dp[3] is now min(3, 1) = 1.
# Result: dp is now [0, 1, 2, 1, inf, inf, inf]
# a = 4: How to make 4?
# Try coin = 1: 1 + dp[3] = 1 + 1 = 2. dp[4] becomes 2.
# Try coin = 3: 1 + dp[1] = 1 + 1 = 2. dp[4] is still min(2, 2) = 2.
# Try coin = 4: 1 + dp[0] = 1 + 0 = 1. dp[4] is now min(2, 1) = 1.
# Result: dp is now [0, 1, 2, 1, 1, inf, inf]
# a = 5: How to make 5?
# Try coin = 1: 1 + dp[4] = 1 + 1 = 2. dp[5] becomes 2.
# Try coin = 3: 1 + dp[2] = 1 + 2 = 3. dp[5] is still min(2, 3) = 2.
# Try coin = 4: 1 + dp[1] = 1 + 1 = 2. dp[5] is still min(2, 2) = 2.
# Result: dp is now [0, 1, 2, 1, 1, 2, inf]
# a = 6: How to make 6?
# Try coin = 1: 1 + dp[5] = 1 + 2 = 3. dp[6] becomes 3.
# Try coin = 3: 1 + dp[3] = 1 + 1 = 2. dp[6] is now min(3, 2) = 2.
# Try coin = 4: 1 + dp[2] = 1 + 2 = 3. dp[6] is still min(2, 3) = 2.
# Result: dp is now [0, 1, 2, 1, 1, 2, 2]
# The outer loop finishes. We have solved the problem for every sub-amount.