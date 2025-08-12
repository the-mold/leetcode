class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] will be storing the number of combinations for amount i
        dp = [0] * (amount + 1)

        # Base case: There is one way to make amount 0 (by using no coins)
        dp[0] = 1

        # Iterate through each coin. This order prevents counting permutations.
        for coin in coins:
            # For each coin, update the dp array for all amounts it can contribute to.
            for a in range(coin, amount + 1):
                # The number of ways to make amount 'a' is increased by the number
                # of ways to make amount 'a - coin'.
                dp[a] += dp[a - coin]

        return dp[amount]




# Building with One Coin at a Time
# To count unique combinations, we build our solution by iterating through each coin one by one and calculating its contribution to all possible amounts.

# The DP State:

# dp[i] will store the number of unique combinations that sum up to amount i.
# The Logic:

# Initialization:
# Create a dp array of size amount + 1, initialized to all zeros.
# Set the crucial base case: dp[0] = 1. This signifies that there is exactly one way to make an amount of 0: by choosing no coins. This is the foundation of all our calculations.
# Looping Strategy (The Key Change):
# The outer loop iterates through each coin in the coins list.
# The inner loop iterates through the amounts, from the value of the current coin up to the target amount.
# The Recurrence Relation:
# For each coin, as we iterate through the amounts a, we update our dp table. The logic is: "The new number of ways to make amount a is whatever it was before, PLUS the number of ways we could make a - coin."
# In code: dp[a] += dp[a - coin]
# By processing one coin at a time for all amounts, we ensure that combinations like {1, 2} and {2, 1} are only counted once.
# Step-by-Step Example
# Let's trace coins = [1, 2, 5] and amount = 5.

# Initial State: dp = [1, 0, 0, 0, 0, 0]

# 1. Processing coin = 1: We update dp[a] for a from 1 to 5.

# dp[1] += dp[0] -> dp[1] = 1 ({1})
# dp[2] += dp[1] -> dp[2] = 1 ({1,1})
# dp[3] += dp[2] -> dp[3] = 1 ({1,1,1})
# dp[4] += dp[3] -> dp[4] = 1 ({1,1,1,1})
# dp[5] += dp[4] -> dp[5] = 1 ({1,1,1,1,1}) dp array is now: [1, 1, 1, 1, 1, 1] (ways to make change using only pennies)
# 2. Processing coin = 2: We update dp[a] for a from 2 to 5.

# dp[2] += dp[0] -> dp[2] = 1 + 1 = 2 (new way: {2})
# dp[3] += dp[1] -> dp[3] = 1 + 1 = 2 (new way: {1,2})
# dp[4] += dp[2] -> dp[4] = 1 + 2 = 3 (new ways: {2,2}, {1,1,2})
# dp[5] += dp[3] -> dp[5] = 1 + 2 = 3 (new ways: {1,2,2}, {1,1,1,2}) dp array is now: [1, 1, 2, 2, 3, 3]
# 3. Processing coin = 5: We update dp[a] for a from 5 to 5.

# dp[5] += dp[0] -> dp[5] = 3 + 1 = 4 (new way: {5}) dp array is now: [1, 1, 2, 2, 3, 4]
# Final Answer: The loop finishes. The answer is dp[amount], which is dp[5] = 4. The 4 combinations are: {1,1,1,1,1}, {1,1,1,2}, {1,2,2}, {5}.

# I will now create a new file coin_change_2.py with the code for this solution.