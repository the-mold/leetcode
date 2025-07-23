class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left <= right:
        mid = (left + right) // 2

        hours_needed_to_eat_all = 0
        for pile in piles:
            hours_needed_to_eat_all += math.ceil(pile / mid)
        
        if hours_needed_to_eat_all <= h:
            res = min(mid, res)
            right = mid - 1
        else:
            left = mid + 1

    return res
  
# Time Complexity: O(n log m)
# The solution has two main components:

# Binary Search Loop: O(log m)
# m is the maximum pile size (max(piles))
# The binary search space starts from 1 to max(piles)
# In each iteration, we divide the search space in half
# This gives us O(log m) iterations
# Calculation of Hours Needed: O(n)
# For each potential eating speed (mid value), we iterate through all n piles
# For each pile, we calculate math.ceil(pile / mid)
# This operation is O(1) for each pile
# So, the total is O(n) for all piles
# Since we perform the O(n) calculation for each of the O(log m) binary search iterations, the overall time complexity is O(n log m), where:

# n is the number of piles
# m is the maximum pile size
# Space Complexity: O(1)
# The solution uses only a constant amount of extra space:

# left, right, and res are single integer variables
# mid
#  and hours_needed_to_eat_all are also single integer variables
# No additional data structures are created that scale with input size
# Therefore, the space complexity is O(1) (constant space).

# Optimization Note
# This is an efficient solution using binary search on the answer space. The algorithm correctly finds the minimum eating speed k such that Koko can eat all bananas within h hours.