class Solution:
    def numTeams(self, rating: List[int]) -> int:
        memo = {}
        n = len(rating)

        def helper(i: int, taken: int, is_increasing: bool):
            if taken == 3:
                return 1
            
            key = (i, taken, is_increasing)
            if key in memo:
                return memo[key]
            
            res = 0
            if is_increasing:
                for idx in range(i + 1, n):
                    if rating[idx] > rating[i]:
                        res += helper(idx, taken + 1, True)
            else:
                for idx in range(i + 1, n):
                    if rating[idx] < rating[i]:
                        res += helper(idx, taken + 1, False)

            memo[key] = res
            return res
        
        
        total = 0
        for i in range(n):
            total += helper(i, 1, True)
            total += helper(i, 1, False)
        
        return total


# Complexity Analysis
# Let n be the length of the rating array.

# Time complexity: O(n 
# 2
#  )

# The algorithm iterates through rating, each time calling countIncreasingTeams and countDecreasingTeams. In the worst case, the recursive functions might explore all subsequent soldiers for each call. However, due to memoization, each unique subproblem is only computed once. There are n possible indices and 3 possible team sizes (1,2,3). This gives us n×3=O(n) unique sub-problems. Each sub-problem may iterate through up to n soldiers in the worst case. Therefore, the overall time complexity is O(n 
# 2
#  ).

# Space complexity: O(n)

# Each cache (increasingCache and decreasingCache) is a 2D array of size n×4, thus taking O(8⋅n)=O(n) space.

# The maximum depth of recursion is 3, so this doesn't add to the asymptotic space complexity.

# Thus, the overall space complexity is O(n).