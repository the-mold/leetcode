class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def solve(idx, prev_idx):
            if idx >= n:
                return 0

            key = (idx, prev_idx)
            if key in memo:
                return memo[key]

            # choice 1: skip current idx
            len_if_skip = solve(idx + 1, prev_idx)

            len_if_counted = 0
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                len_if_counted = 1 + solve(idx + 1, idx)

            res = max(len_if_skip, len_if_counted)

            memo[key] = res
            return res
            
        return solve(0, -1)

# Time Complexity: O(n²)
# The time complexity is determined by the number of unique states that the recursive function _max_increasing_subseq can be called with, as each state is computed only once due to memoization._

# The state is defined by the memoization key: (idx, prev_number).
# idx: This parameter can range from 0 to n, where n is the length of the numbers list. This gives n + 1 possible values.
# prev_number: This parameter can be any of the numbers from the input list, plus the initial float("-inf"). In the worst case, if all numbers are unique, this gives n + 1 possible values.
# Therefore, the total number of unique states is approximately (n + 1) * (n + 1), which is O(n²). Since the work done within each function call (excluding recursion) is constant, the total time complexity is O(n²).*

# Space Complexity: O(n²)
# The space complexity is determined by two factors: the recursion stack depth and the space used for memoization.

# Memoization Table: The memo dictionary stores the result for each unique state (idx, prev_number). As established, there are O(n²) such states. Therefore, the memoization table requires O(n²) space.
# Recursion Stack: The maximum depth of the recursion is n, as the idx parameter increments by 1 in each call. This contributes O(n) to the space complexity.
# The space required for the memoization table dominates the recursion stack depth. Thus, the overall space complexity is O(n²).