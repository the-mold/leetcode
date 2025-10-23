from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def solve(i, curr_total):
            # warning! you check this base case after all numbers are processed, hence len(nums) and not len(nums) - 1.
            if i == len(nums):
                return 1 if curr_total == target else 0

            # (i, curr_total) What are the number of ways to reach the target if we are at index i and our current sum is curr_total?
            if (i, curr_total) in memo:
                return memo[(i, curr_total)]

            # Calculate the number of ways by branching out:
            # 1. Add the current number (nums[i]) and move to the next element.
            # 2. Subtract the current number (nums[i]) and move to the next element.
            # The total is the sum of ways from both branches.
            res = solve(i + 1, curr_total + nums[i]) + solve(i + 1, curr_total - nums[i])
            memo[(i, curr_total)] = res
            return res

        res= solve(0,0)
        return res


s = Solution()
s.findTargetSumWays([1,1,1,1,1], 3)


# Time and space
# Let:

# n be the number of elements in the nums list.
# S be the sum of all numbers in nums.
# Time Complexity: O(n * S)
# Without Memoization (Brute Force): For each of the n numbers, you have two choices: add or subtract. This leads to 2^n possible combinations. The time complexity would be O(2^n), which is very slow.
# With Memoization: The memoization technique ensures that each unique subproblem is solved only once. A subproblem is defined by the state (i, curr_total).
# The index i can range from 0 to n. That's n+1 possible values.
# The curr_total can range from -S (if we subtract all numbers) to +S (if we add all numbers). The total range of possible sums is 2 * S + 1.
# The total number of unique states (i, curr_total) is therefore approximately n * (2 * S).
# Since each state is computed only once, the time complexity is the number of states we need to fill in our memo dictionary.

# Therefore, the time complexity is O(n * S).

# Space Complexity: O(n * S)
# The space complexity is determined by two factors: the recursion depth and the size of the memo dictionary.

# Recursion Stack Depth: In the worst case, the recursion can go n levels deep (from i=0 to i=n). This contributes O(n) to the space complexity.
# memo Dictionary: The memo dictionary stores the result for every unique state (i, curr_total). As we established, there are O(n * S) possible states. In the worst case, the dictionary will store all of them.
# The space required for the memo dictionary, O(n * S), dominates the space required for the recursion stack, O(n).

# Therefore, the overall space complexity is O(n * S).






# trace
# Let's trace the logic with a simple example: nums = [1, 1, 1] and target = 1.

# The goal is to find how many ways we can put + or - in front of each number to make the total sum equal to 1. The possible ways are:

# +1 +1 -1 = 1
# +1 -1 +1 = 1
# -1 +1 +1 = 1 So the answer should be 3.
# The code solves this using a technique called recursion with memoization.

# Step-by-Step Breakdown
# The main logic happens inside the solve(i, curr_total) function.

# i: The index of the number we are currently looking at in the nums array.
# curr_total: The sum we have accumulated so far.
# 1. The Initial Call: solve(0, 0)

# We start the process by calling solve(0, 0). This means: "Let's start at index 0 with a current total of 0."

# 2. Inside solve(0, 0)

# i is 0, curr_total is 0. The number is nums[0], which is 1.
# The code must now explore two branches for the number 1:
# Add it: Call solve(1, 0 + 1), which is solve(1, 1).
# Subtract it: Call solve(1, 0 - 1), which is solve(1, -1).
# The result of solve(0, 0) will be the sum of the results from these two calls. res = solve(1, 1) + solve(1, -1)
# This creates a tree of calls:

#                       solve(0, 0)
#                      /           \
#               solve(1, 1)      solve(1, -1)
# 3. Deeper into the Tree: solve(1, 1) and solve(1, -1)

# Let's follow the left branch first, solve(1, 1):

# i is 1, curr_total is 1. The number is nums[1], which is 1.
# It also splits into two branches:
# Add it: solve(2, 1 + 1) -> solve(2, 2)
# Subtract it: solve(2, 1 - 1) -> solve(2, 0)
# Now let's follow the right branch, solve(1, -1):

# i is 1, curr_total is -1. The number is nums[1], which is 1.
# It splits:
# Add it: solve(2, -1 + 1) -> solve(2, 0)
# Subtract it: solve(2, -1 - 1) -> solve(2, -2)
# The call tree now looks like this:

#                       solve(0, 0)
#                      /           \
#               solve(1, 1)      solve(1, -1)
#              /         \        /          \
#       solve(2, 2)  solve(2, 0)  solve(2, 0)  solve(2, -2)
# 4. The Role of Memoization (The memo Dictionary)

# Notice that solve(2, 0) is called twice. The first time it's called, the code will:

# Calculate its result.
# Store it: memo[(2, 0)] = result.
# The second time solve(2, 0) is called, the code will hit this line: if (i, curr_total) in memo: Since (2, 0) is now a key in our memo dictionary, it will immediately return the stored value instead of re-calculating everything below it. This is what makes the algorithm fast.

# 5. The Base Case (The End of a Path)

# Let's trace one path all the way down, for example solve(2, 2):

# i is 2, curr_total is 2. The number is nums[2], which is 1.
# It splits:
# solve(3, 2 + 1) -> solve(3, 3)
# solve(3, 2 - 1) -> solve(3, 1)
# Now, let's look at solve(3, 1):

# i is 3.
# The code hits the base case: if i == len(nums): (since 3 == len([1, 1, 1])).
# It then checks: return 1 if curr_total == target else 0.
# Here, curr_total is 1 and target is 1. They match! So it returns 1. This means we found one valid way to reach the target down this path (+1 +1 -1).
# Now look at solve(3, 3):

# i is 3.
# It hits the base case.
# curr_total is 3, target is 1. They don't match. It returns 0.
# 6. Rolling Back Up

# The results are passed back up the tree and added together.

# The call to solve(2, 2) gets the results from its children: 0 + 1 = 1. It stores memo[(2, 2)] = 1 and returns 1.
# This process continues all the way back to the top. solve(0, 0) will eventually sum up all the 1s returned from the valid paths at the bottom of the tree.
# The final tree shows which paths result in 1 (a success) and which result in 0 (a failure) at the very end. Summing them up gives the total number of ways.