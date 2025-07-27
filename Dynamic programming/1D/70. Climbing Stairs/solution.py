class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

#T:O(n)
#S:O(n)

# Intuition
#1. Create array with stair indexes. 0 is the start - no step at all 
#2. For each step we calculate how many ways is there to get to it. For step 1, you know it is 1.
#For stair 2 you can get in two ways: 1+1 or 2. That is why number of combination for stair 2 is 2.
#Assign both to your array.
#3. Loop through other steps from lower steps to the top. To get value for each stair, this is the sum of
#two previous stairs. This gives the total ways you can get to a stair.
#4. The last element in your array contains the result for you `n`th stair in problem.


# Why use n+1?
# The main reason for using an array of size n + 1 is for convenience and code clarity. It allows us to have a direct, one-to-one mapping between the step number and the array index.

# Here's the breakdown:

# Problem Domain: We are solving for steps 1, 2, 3, ..., n. We want to find the number of ways to get to each of these steps.
# Array Indexing: In Python (and most programming languages), arrays are 0-indexed. This means if you create an array of size n, its indices will range from 0 to n-1.
# The Mismatch: If we use an array of size n, we have indices [0, 1, ..., n-1]. To store the result for step n, we would have to put it at index n-1. This means the result for any step i would be stored at index i-1. The code would look like this: