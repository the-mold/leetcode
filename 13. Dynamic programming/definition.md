# At its core, Dynamic Programming is an algorithmic technique for solving a complex problem by breaking it down into a collection of simpler, overlapping subproblems. The key idea is to solve each subproblem only once and store its result, avoiding redundant computations.

# A problem can be solved using Dynamic Programming if it has two key characteristics:

# Optimal Substructure: An optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems. For example, to find the shortest path from A to C, if it passes through B, then the path from A to B must also be the shortest possible.
# Overlapping Subproblems: A recursive algorithm solves the same subproblems over and over again, rather than generating new subproblems. DP takes advantage of this by computing the solution to each subproblem just once and storing it in a cache (like a hash map or an array).
# Two Main Approaches to DP
# There are two primary ways to implement a DP solution:

# 1. Top-Down with Memoization
# This is a recursive approach. You write a standard recursive function to solve the problem, but you "memoize" the results.

# How it works:
# Create a cache (e.g., an array or a hash map) to store the results of subproblems.
# In your recursive function, before computing the solution for a subproblem, first check if the result is already in the cache.
# If it is, return the cached result.
# If it's not, compute the result, store it in the cache, and then return it.
# This approach is often more intuitive because it follows the natural logic of the recursive formula.

# Example (Fibonacci):

# python
# def fib(n, memo={}):
#     if n in memo: return memo[n]
#     if n <= 1: return n
    
#     memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]

# 2. Bottom-Up with Tabulation
# This is an iterative approach. You build a table (usually an array or a 2D grid) and fill it up from the "bottom" (the smallest subproblems) to the "top" (the final solution).

# How it works:
# Figure out the dimensions of the table (DP array).
# Initialize the base cases in the table.
# Write a loop that iterates through the table and calculates the solution for each subproblem based on the results of previously solved subproblems.
# The final answer is the last entry in the table.
# This approach often has slightly better performance as it avoids the overhead of recursion. The Tribonacci solution we just worked on is a perfect example of this.

# Example (Fibonacci):

# python
# def fib(n):
#     if n <= 1: return n
    
#     dp = [0] * (n + 1)
#     dp[1] = 1
    
#     for i in range(2, n + 1):
#         dp[i] = dp[i-1] + dp[i-2]
        
#     return dp[n]


# Classic DP Problems for Interviews
# Here are some must-know DP problems. Practicing these will build a strong foundation.

# 1D DP (using a simple array):
# Fibonacci / Tribonacci Sequence
# Climbing Stairs
# Coin Change (find the minimum number of coins)
# House Robber
# Longest Increasing Subsequence (LIS)

# 2D DP (using a grid):
# Unique Paths
# Longest Common Subsequence (LCS)
# 0/1 Knapsack Problem
# Edit Distance
# Regular Expression Matching
# How to Spot a DP Problem in an Interview
# Look for these clues:

# The problem asks for the maximum/minimum/longest/shortest value or asks to count the number of ways to do something.
# You can define the state of the problem with a few discrete variables (e.g., dp(i) or dp(i, j)).
# A naive recursive solution would be very slow because it re-computes the same subproblems many times.



# Choose n or n+1 as dp length?
# The choice is all about convenience and clarity.

# Use n+1 when the problem is defined in terms of 1 to n items/steps, and you need to find the value for n.
# Use n when the problem is defined by a 0-indexed array of length n, and the states map directly to the indices of that array.