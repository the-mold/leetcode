class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        n = len(questions)

        def solve(question_idx):
            # you left the boundtries of questions array. You get 0 pointes here.
            if question_idx >= n:
                return 0

            if question_idx in memo:
                return memo[question_idx]

            next_question_if_solve_current = question_idx + questions[question_idx][1] + 1
            points_when_solve_current_question = questions[question_idx][0] + solve(next_question_if_solve_current)
            points_when_skip_current_question = solve(question_idx+1)

            res = max(points_when_solve_current_question, points_when_skip_current_question)

            memo[question_idx] = res
            return res

        # how much points i earn if i start from 0 indexed question
        return solve(0)
      
# Time Complexity: O(n)
# Without Memoization (Brute-Force): If you didn't use the memo dictionary, at each question i, you would branch into two recursive calls (solve(i+1) and solve(i + brainpower + 1)). This would create a tree of calls that could explore the same subproblems many times, leading to an exponential time complexity, roughly O(2^n).
# With Memoization: The memo dictionary is the key to improving the performance.
# Subproblems: The problem is broken down into subproblems defined by the state solve(question_idx). The only variable that defines a subproblem is question_idx.
# Number of Subproblems: The question_idx can range from 0 to n-1. This means there are at most n unique subproblems to solve.
# Work per Subproblem: For each subproblem solve(i), the function performs a constant amount of work: a few arithmetic operations, a max comparison, and two recursive calls. Because of memoization, the actual computation for any given solve(i) happens only once. Any subsequent call with the same i is an O(1) dictionary lookup.
# Since there are n unique subproblems and each takes O(1) time to compute (the first time it's called), the total time complexity is the number of subproblems multiplied by the work per subproblem.

# Total Time Complexity = n * O(1) = O(n)

# Space Complexity: O(n)
# The space complexity is determined by the storage used by the memo dictionary and the depth of the recursion stack.

# Memoization Dictionary (memo): In the worst case, the memo dictionary will store the result for every single index from 0 to n-1. This means the dictionary can grow to have up to n key-value pairs. This requires O(n) space.
# Recursion Stack: The recursion depth determines the space used by the call stack. In the worst-case scenario, you could have a chain of "skip" decisions (solve(i+1)), leading to a recursion depth of n. For example, solve(0) calls solve(1), which calls solve(2), and so on, until solve(n). This also requires O(n) space.
# Since both the memo dictionary and the recursion stack can take up to O(n) space, the total space complexity is dominated by these factors.

# Total Space Complexity = O(n) (for the memo dictionary) + O(n) (for the recursion stack) = O(n)